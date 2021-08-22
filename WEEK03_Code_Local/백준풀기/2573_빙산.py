import sys
import copy

sys.setrecursionlimit(10000000000)

N, M  = map(int, sys.stdin.readline().strip().split())

glacier = []
for _ in range(N):
    glacier.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

checker = [[0] * M for _ in range(N)]

def count_water(x, y):
    count = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] == 0:
            count += 1
    return count

def dfs(x, y):
    checker[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] > 0:
            if checker[new_x][new_y] == 0:
                checker[new_x][new_y] = 1
                dfs(new_x, new_y)

glacier_count = 1
count = 0
year = 0

copy_glacier = copy.deepcopy(glacier)
while count < 2 and glacier_count > 0:
    glacier_count = 0
    count = 0

    for i in range(N):
        for j in range(M):
            if glacier[i][j] != 0:
                copy_glacier[i][j] -= count_water(i, j)
                if copy_glacier[i][j] < 0:
                    copy_glacier[i][j] = 0
    for p in range(N):
        for q in range(M):
            if checker[p][q] == 0 and copy_glacier[p][q] > 0:
                glacier_count += 1
                dfs(p, q)
                count += 1
    year += 1


### 1년이 지날 때, 빙하였다가 물이 된 타일이 이후에 count_water에서 물로 카운트 된다!!!  -> deepcopy로 해결, 공간복잡도는 안좋아짐
### dfs로 RecursionError -> OverflowError  dfs로는 힘들듯??
print(year)

