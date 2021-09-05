# https://www.acmicpc.net/problem/1520
# 내리막길

import collections
import sys
read = sys.stdin.readline

sys.setrecursionlimit(30000)

M, N = map(int, read().strip().split())
graph = [list(map(int, read().strip().split())) for _ in range(M)]


dp = [[0] * N for _ in range(M)]
dp[M - 1][N - 1] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_path(x, y):
    visited = [[0] * N for _ in range(M)]

    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] > graph[x][y]:
            if visited[nx][ny] == 0:
                temp += find_path(nx, ny)
                dp[nx][ny] += temp
    visited[x][y] = 1
    return dp[x][y]

find_path(M - 1, N - 1)
for i in dp:
    print(i)









## 시간초과
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]


# visited = [[0] * N for _ in range(M)]
# count = 0

# def dfs(x, y):
#     global count
#     visited[x][y] = 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx == M - 1 and ny == N - 1:
#             count += 1

#         if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < graph[x][y]:
#             if visited[nx][ny] == 0:
#                 dfs(nx, ny)
#                 visited[nx][ny] = 0

# dfs(0, 0)
# print(count)


