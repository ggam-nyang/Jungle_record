import sys

sys.setrecursionlimit(10000)
M, N = map(int, sys.stdin.readline().strip().split())

height_map = []

for _ in range(M):
    height_map.append(list(map(int, sys.stdin.readline().strip().split())))

## dp를 이용!!!
visited = [[-1] * N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited[M - 1][N - 1] = 1
count = 0
def dfs(x, y):
    if visited[x][y] != -1:
        return visited[x][y]


    temp = 0

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < M and 0 <= new_y < N and height_map[x][y] > height_map[new_x][new_y]:
            temp += dfs(new_x, new_y)

    visited[x][y] = temp

    return visited[x][y]
    # for e in checker:
    #     print(e)
    # print()
ans = dfs(0, 0)
print(ans)