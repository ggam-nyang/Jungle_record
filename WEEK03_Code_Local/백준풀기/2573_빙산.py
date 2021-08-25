import sys
import collections

### 너무 크면 메모리를 잡아먹는다!!!
sys.setrecursionlimit(10000)

N, M  = map(int, sys.stdin.readline().strip().split())

glacier = []
for _ in range(N):
    glacier.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

## 주변에 물이 몇개인지 세주는 함수
def count_water(x, y):
    count = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] == 0:
            count += 1
    return (x, y, count)

## dfs를 이용하여, 이어진 land를 탐색
def dfs(x, y):
    checker[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] > 0:
            if checker[new_x][new_y] == 0:
                checker[new_x][new_y] = 1
                dfs(new_x, new_y)


## bfs를 이용하여, 이어진 land를 탐색
queue = collections.deque()
def bfs(x, y):
    queue.append((x, y))
    checker[x][y] = 1
    while queue:
        p, q = queue.popleft()

        for i in range(4):
            new_x = p + dx[i]
            new_y = q + dy[i]

            if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] > 0:
                if checker[new_x][new_y] == 0:
                    checker[new_x][new_y] = 1
                    queue.append((new_x, new_y))






glacier_count = 1
count = 0
year = 0

melting_list = []
## 이어진 land가 2개 이상이거나, land가 0개라면 종료!
while count < 2 and glacier_count > 0:
    glacier_count = 0
    count = 0
    checker = [[0] * M for _ in range(N)]
## bfs, dfs 모두 사용 가능하다. 이어진 땅 덩어리를 탐색
    for p in range(N):
        for q in range(M):
            if checker[p][q] == 0 and glacier[p][q] > 0:
                glacier_count += 1
                bfs(p, q)
                count += 1
## 땅이 두개 이상이면 종료!
    if count > 1:
        break

## 각 지점의 melting 되는 양을 담아두고, 한번에 처리.
    for i in range(N):
        for j in range(M):
            if glacier[i][j] != 0:
                melting_list.append(count_water(i, j))
    while melting_list:
        x, y, melt = melting_list.pop()
        glacier[x][y] -= melt
        if glacier[x][y] < 0:
            glacier[x][y] = 0
    year += 1


if count < 2:
    print(0)
else:
    print(year)

