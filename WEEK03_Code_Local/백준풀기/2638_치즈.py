import sys
import collections



N, M = map(int, sys.stdin.readline().strip().split())

cheese_list = []
for _ in range(N):
    cheese_list.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


### 블로그 참고
def real_bfs():
    queue = collections.deque()
    queue.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] == 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if cheese_list[nx][ny] >= 1:
                        cheese_list[nx][ny] += 1
                    else:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
hour = 0
while True:
    real_bfs()
    count = 0

    for i in range(N):
        for j in range(M):
            if cheese_list[i][j] >= 3:
                cheese_list[i][j] = 0
                count += 1
            elif cheese_list[i][j] == 2:
                cheese_list[i][j] = 1
    if count == 0:
        break
    else:
        hour += 1
print(hour)







### 시간초과
def cheese_bfs(x, y, check):
    cheese_queue = collections.deque()
    cheese_queue.append((x, y))
    check[x][y] = 1

    exposed_cheese = []
    while cheese_queue:
        p, q = cheese_queue.popleft()
        temp = 0
        for i in range(4):
            nx = p + dx[i]
            ny = q + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if cheese_list[nx][ny] == 2:
                    temp += 1
                elif cheese_list[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    cheese_queue.append((nx, ny))

        if temp > 1:
            exposed_cheese.append((p, q))

    if exposed_cheese:
        for ex, ey in exposed_cheese:
            cheese_list[ex][ey] = 2




def check_out_air(x, y, check):
    air_queue = collections.deque()
    air_queue.append((x, y))
    check[x][y] = 1


    while air_queue:
        p, q = air_queue.popleft()
        cheese_list[p][q] = 2
        for i in range(4):
            nx = p + dx[i]
            ny = q + dy[i]

            if 0 <= nx < N and 0 <= ny < M and cheese_list[nx][ny] == 0:
                if check[nx][ny] == 0:
                    check[nx][ny] = 1
                    air_queue.append((nx, ny))



out_air_process = False
cheese_count = 1
year = 0
while cheese_count > 0:
    checker = [[0] * M for _ in range(N)]
    cheese_count = 0
    for i in range(N):
        for j in range(M):

            if cheese_list[i][j] == 1 and checker[i][j] == 0:
                cheese_count += 1
                cheese_bfs(i, j, checker)
                year += 1

            elif cheese_list[i][j] == 0 and out_air_process == False:
                check_out_air(i, j, checker)
                out_air_process = True


# print(year)
# print(cheese_list)