#include <stdio.h>
#include "csapp.h"

/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400

/* You wo n't lose style points for including this long line in your code */
static const char *user_agent_hdr =
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 "
    "Firefox/10.0.3\r\n";

void doit(int fd);
void parse_uri(char *uri, char *hostname, char *path, int *port);
void build_http_header(char *http_header, char *hostname, char *path, int port, rio_t *client_rio);
int connect_endServer(char *hostname, int port, char *http_header);




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
    clientlen = sizeof(clientaddr); // 생각해보기
    connfd = Accept(listenfd, (SA *)&clientaddr,
                    &clientlen);  // line:netp:tiny:accept
    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE,
                0);
    printf("Accepted connection from (%s, %s)\n", hostname, port);
    doit(connfd);   // line:netp:tiny:doit
    Close(connfd);  // line:netp:tiny:close
  }
  return 0;
}

void doit(int fd)
{
  int end_serverfd;

  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];
  char endserver_http_header[MAXLINE];
  // request line 저장용
  char hostname[MAXLINE], path[MAXLINE];
  int port;

  rio_t rio, server_rio;

  Rio_readinitb(&rio, fd);
  Rio_readlineb(&rio, buf, MAXLINE);
  sscanf(buf, "%s %s %s", method, uri, version);
  if (strcasecmp(method, "GET")) {
    printf("Proxy does not implement the method");
    return;
  }

  parse_uri(uri, hostname, path, &port);

  build_http_header(endserver_http_header, hostname, path, port, &rio);

  end_serverfd = connect_endServer(hostname, port, endserver_http_header);
  if (end_serverfd < 0)
  {
    printf("Connection failed\n");
    return;
  }

  Rio_readinitb(&server_rio, end_serverfd);
  Rio_writen(end_serverfd, endserver_http_header, strlen(endserver_http_header));

  size_t n;
  while ((n = Rio_readlineb(&server_rio, buf, MAXLINE)) != 0)
  {
    printf("proxy received %d bytes, then send\n", n);
    Rio_writen(fd, buf, n);
  }
  Close(end_serverfd);
}



void parse_uri(char *uri, char *hostname, char *path, int *port)
{
  *port = 80;
  char *pos = strstr(uri, "//");  // 뭘 의미하나?

  pos = pos != NULL ? pos + 2: uri;

  char *pos2 = strstr(pos, ":");
  if (pos2 != NULL)
  {
    *pos2 = '\0';
    sscanf(pos, "%s", hostname);
    sscanf(pos2 + 1, "%d%s", port, path);
  }
  else
  {
    pos2 = strstr(pos, "/");
    if (pos2 != NULL)
    {
      *pos2 = '\0';
      sscanf(pos, "%s", hostname);
      *pos2 = '/';
      sscanf(pos2, "%s", path);
    }
    else
    {
      sscanf(pos, "%s", hostname);
    }
  }
  return;
}

void build_http_header(char *http_header, char *hostname, char *path, int port, rio_t *client_rio)
{
  char buf[MAXLINE], request_hdr[MAXLINE], other_hdr[MAXLINE], host_hdr[MAXLINE];

  sprintf(request_hdr, "GET %s HTTP/1.0\r\n", path);

  while (Rio_readlineb(client_rio, buf, MAXLINE) > 0)
  {
    if (strcmp(buf, "\r\n") == 0)
      break;

    if (!strncasecmp(buf, "Host", strlen("Host")))
    {
      strcpy(host_hdr, buf);
      continue;
    }

    if (!strncasecmp(buf, "Connection", strlen("Connection"))
       && !strncasecmp(buf, "Proxy-Connection: close\r\n", strlen("Proxy-Connection: close\r\n"))
       && !strncasecmp(buf, "User-Agent", strlen("User-Agent")))
    {
      strcat(other_hdr, buf);
    }
  }
  if (strlen(host_hdr) == 0)
  {
    sprintf(host_hdr, "Host: %s\r\n", hostname);
  }
  sprintf(http_header, "%s%s%s%s%s%s%s", request_hdr, host_hdr, "Connection: close\r\n", "Proxy-Connection: close\r\n", "User-Agent", other_hdr, "\r\n");

  return;
}

inline int connect_endServer(char *hostname, int port, char *http_header)
{
  char portStr[100];
  sprintf(portStr, "%d", port);
  return Open_clientfd(hostname, portStr);
}