import sys
import collections
## 입력 받기
M, N, H = map(int, sys.stdin.readline().strip().split())

tomato_box = [[] for _ in range(H)]

for i in range(H):
    for j in range(N):
        line = list(map(int, sys.stdin.readline().strip().split()))
        tomato_box[i].append(line)

queue = collections.deque()

## 동, 서 , 남, 북 그리고 위, 아래까지 확인하기 위한 배열
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

## x, y, z 값이 주어졌을 때 인접한 익지 않은 토마토를 queue에 넣어주고, 익지 않은 토마토들이 익는데 걸린 시간을 넣어주는 함수
def bfs(arr, x, y, z):
    for i in range(6):
        new_x = x + dx[i]
        new_y = y + dy[i]
        new_z = z + dz[i]

        if (0 <= new_x < M) and (0 <= new_y < N) and (0 <= new_z < H) and (tomato_box[new_z][new_y][new_x] == 0):
            tomato_box[new_z][new_y][new_x] = tomato_box[z][y][x] + 1
            queue.append((new_z, new_y, new_x))

max_time = 1
is_possible = True
empty = 0
## 토마토 상자를 열어보며, 익은 토마토 즉 값이 1인 경우를 queue에 넣어줌. 혹시 1의 개수와 -1의 개수의 합이 전체와 같다면, 모두 익은 것이므로 0을 출력
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato_box[z][y][x] == 1:
                queue.append((z, y, x))
            elif tomato_box[z][y][x] == -1:
                empty += 1
if len(queue) + empty == M * N * H:
    print(0)
else:
    while queue:
        new_tomato = queue.popleft()
        bfs(tomato_box, new_tomato[2], new_tomato[1], new_tomato[0])

    for z in range(H):
        if not is_possible:
            break
        for y in range(N):
            if not is_possible:
                break
            for x in range(M):
                time_to_be_tomato = tomato_box[z][y][x]

                if tomato_box[z][y][x] == 0:
                    is_possible = False
                    break

                if max_time < time_to_be_tomato:
                    max_time = time_to_be_tomato

## 익을 수 없는 토마토가 있으면 -1 출력, 아니라면 max_time - 1 출력 (첫 토마토를 1부터 시작해서 1을 빼준다)
    if is_possible:
        print(max_time - 1)
    else:
        print(-1)