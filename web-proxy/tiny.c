/* $begin tinymain */
/*
 * tiny.c - A simple, iterative HTTP/1.0 Web server that uses the
 *     GET method to serve static and dynamic content.
 *
 * Updated 11/2019 droh
 *   - Fixed sprintf() aliasing issue in serve_static(), and clienterror().
 */
#include "csapp.h"

void doit(int fd);
void read_requesthdrs(rio_t *rp);
int parse_uri(char *uri, char *filename, char *cgiargs);
void serve_static(int fd, char *filename, int filesize, char *method);
void get_filetype(char *filename, char *filetype);
void serve_dynamic(int fd, char *filename, char *cgiargs, char *method);
void clienterror(int fd, char *cause, char *errnum, char *shortmsg,
                 char *longmsg);

void serve_static_head(int fd, char *filename, int filesize);



int main(int argc, char **argv) {
  int listenfd, connfd;
  char hostname[MAXLINE], port[MAXLINE];
  socklen_t clientlen;
  struct sockaddr_storage clientaddr;

  /* Check command line args */
  if (argc != 2) {
    fprintf(stderr, "usage: %s <port>\n", argv[0]);
    exit(1);
  }

  listenfd = Open_listenfd(argv[1]);
  while (1) {
    clientlen = sizeof(clientaddr);
    connfd = Accept(listenfd, (SA *)&clientaddr,
                    &clientlen);  // line:netp:tiny:accept
    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE,
                0);
    printf("Accepted connection from (%s, %s)\n", hostname, port);
    doit(connfd);   // line:netp:tiny:doit
    Close(connfd);  // line:netp:tiny:close
  }
}
void doit(int fd)
{
  int is_static;
  struct stat sbuf;
  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];
  char filename[MAXLINE], cgiargs[MAXLINE];
  rio_t rio;

  // 요청 라인을 읽고 분석한다.
  Rio_readinitb(&rio, fd);
  Rio_readlineb(&rio, buf, MAXLINE);
  printf("Request headers: \n");
  printf("%s", buf);
  sscanf(buf, "%s %s %s", method, uri, version);
  // GET 메소드만 받겠다!!
  if (strcasecmp(method, "GET") == 0 || strcasecmp(method, "HEAD") == 0) {
    read_requesthdrs(&rio); // 다른 요청 헤더를 무시한다.

    // GET 요청으로부터 URI를 가져온다.
    is_static = parse_uri(uri, filename, cgiargs);
    if (stat(filename, &sbuf) < 0) {
      clienterror(fd, filename, "404", "Not found", "Tiny couldn't find this file");
      return ;
    }
    // 보통 파일이고 읽기 권한이 있는지!
    if (is_static) {
      if (!(S_ISREG(sbuf.st_mode)) || !(S_IRUSR & sbuf.st_mode)) {
        clienterror(fd, filename, "403", "Forbidden", "Tiny couldn't read the file");
        return;
      }
      serve_static(fd, filename, sbuf.st_size, method); // 정적 콘텐츠 클라이언트에게 제공
    }
    else {
      if (!(S_ISREG(sbuf.st_mode)) || !(S_IXUSR & sbuf.st_mode)) {
        clienterror(fd, filename, "403", "Forbidden", "Tiny couldn't read the file");
        return;
      }
      serve_dynamic(fd, filename, cgiargs, method); // 동적 콘텐츠 클라이언트에게 제공
    }
  }
  
  else {
    clienterror(fd, method, "501", "Not implemented", "Tiny does not implement this method");
    return ;
  }
}


void clienterror(int fd, char *cause, char *errnum, char *shortmsg, char *longmsg)
{
  char buf[MAXLINE], body[MAXLINE];
  
  /* HTTP 응답 body 만들기 */
  sprintf(body, "<html><title>Tiny Error</title>");
  sprintf(body, "%s<body bgcolor=""ffffff"">\r\n", body);
  sprintf(body, "%s%s: %s\r\n", body, errnum, shortmsg);
  sprintf(body, "%s<p>%s: %s\r\n", body, longmsg, cause);
  sprintf(body, "%s<hr><em>The Tiny Web server</em>\r\n",  body);

  // HTTP 응답 출력하기
  sprintf(buf, "HTTP/1.0 %s %s\r\n", errnum, shortmsg);
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Content-type: text/html\r\n");
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Contetn-length: %d\r\n\r\n", (int)strlen(body));
  Rio_writen(fd, buf, strlen(buf));
  Rio_writen(fd, body, strlen(body));
}

void read_requesthdrs(rio_t *rp)
{
  char buf[MAXLINE];

  Rio_readlineb(rp, buf, MAXLINE);
  while(strcmp(buf, "\r\n")) {
    Rio_readlineb(rp, buf, MAXLINE);
    printf("%s", buf);
  }
  return;
}

int parse_uri(char *uri, char *filename, char *cgiargs)
{
  char *ptr;
  char *temp;
  // 정적 콘텐츠라면 cgi-bin을 없애고, filename을 적절히 변경한다.
  if (!strstr(uri, "cgi-bin")) {
    strcpy(cgiargs, "");
    strcpy(filename, ".");
    strcat(filename, uri);
    if (uri[strlen(uri) - 1] == '/')
      strcat(filename, "home.html");
    return 1;
  }
  // 동적 콘텐츠라면 cgi 인자를 추출하고, 나머지 URI부분을 리눅스 파일로 변경
  else {
    ptr = index(uri, '?');
    if (ptr) {
      strcpy(cgiargs, ptr + 1);
      *ptr = '\0';
    }
    else
      strcpy(cgiargs, "");
    strcpy(filename, ".");
    strcat(filename, uri);
    return 0;
  }
}

void serve_static(int fd, char *filename, int filesize, char *method)
{
  int srcfd;
  char *srcp, filetype[MAXLINE], buf[MAXBUF];

  // client에게 response headers 보내기
  get_filetype(filename, filetype);
  sprintf(buf, "HTTP/1.0 200 OK\r\n");
  sprintf(buf, "%sServer: Tiny Web Server\r\n", buf);
  sprintf(buf, "%sConnection: close\r\n", buf);
  sprintf(buf, "%sContent-length: %d\r\n", buf, filesize);
  sprintf(buf, "%sContent-type: %s\r\n\r\n", buf, filetype);
  Rio_writen(fd, buf, strlen(buf));
  printf("Response headers: \n");
  printf("%s", buf);
  

  if (strcasecmp(method, "HEAD")) {
    srcfd = Open(filename, O_RDONLY, 0);
    srcp = (char *)malloc(filesize);
    Rio_readn(srcfd, srcp, filesize);
    // srcp = Mmap(0, filesize, PROT_READ, MAP_PRIVATE, srcfd, 0); // MMap, Munmap 방식의 장/단점을 고민해보자 (brk랑 mmap)!!!
    Close(srcfd);
    Rio_writen(fd, srcp, filesize);
    // Munmap(srcp, filesize);
    free(srcp);
  }
}

void serve_dynamic(int fd, char *filename, char *cgiargs, char *method)
{
  char buf[MAXLINE], *emptylist[] = { NULL };

  sprintf(buf, "HTTP/1.0 200 OK\r\n");
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Server: Tiny Web Server\r\n");
  Rio_writen(fd, buf, strlen(buf));

  if (Fork() == 0) {
    setenv("QUERY_STRING", cgiargs, 1); // QUERY_STRING 환경변수를 URI의 CGI 인자들로 초기화한다!!!
    setenv("REQUEST_METHOD", method, 1); // HEAD method를 위해서!!
    Dup2(fd, STDOUT_FILENO); // STDOUT_FILENO를 가르키던 애가 fd를 가르키게 됨, 이게 자식프로세스가 fd를 가르키게 하는 것
    Execve(filename, emptylist, environ); // CGI 프로그램을 로드하고 실행. filename의 실행코드를 현재 프로세스에 적재하여, 교체하고 새로운 기능으로 실행!!!
  }
  Wait(NULL);
}




void get_filetype(char *filename, char *filetype)
{
  if (strstr(filename, ".html"))
    strcpy(filetype, "text/html");
  else if (strstr(filename, ".gif"))
    strcpy(filetype, "image/gif");
  else if (strstr(filename, ".png"))
    strcpy(filetype, "image/png");
  else if (strstr(filename, ".jpg"))
    strcpy(filetype, "image/jpeg");
  else if (strstr(filename, ".mp4"))
    strcpy(filetype, "image/mp4");
  else
    strcpy(filetype, "text/plain");
}

