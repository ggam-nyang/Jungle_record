import sys
import collections

N = int(sys.stdin.readline().strip())

apartment_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
checker = [[0] * N for _ in range(N)]
queue = collections.deque()

apart_size = []


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 아파트 단지를 찾기 위해 아파트를 탐색
for i in range(N):
    for j in range(N):
        if apartment_list[i][j] == 0:
            checker[i][j] = 1
            continue

# 아파트가 발견되면, 거기서 BFS!!!
        if checker[i][j] == 0:
            count = 0
            queue.append((i, j))
            while queue:
                y, x = queue.popleft()
                checker[y][x] = 1
                count += 1
                for k in range(4):
                    new_x = x + dx[k]
                    new_y = y + dy[k]

                    if 0 <= new_x < N and 0 <= new_y < N and apartment_list[new_y][new_x] == 1:
                        if checker[new_y][new_x] == 0:
                            checker[new_y][new_x] = 1
                            queue.append((new_y, new_x))

            apart_size.append(count)

# 길이와 오름차순으로 단지 내 아파트 개수 출력
print(len(apart_size))
apart_size.sort()
for size in apart_size:
    print(size)