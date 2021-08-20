import sys
import collections
T = int(sys.stdin.readline().strip())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 테스트 케이스 개수만큼 반복
for _ in range(T):
    X, Y, K = map(int, sys.stdin.readline().strip().split())

    baechu_pos = [[0 for _ in range(X)] for _ in range(Y)]

    for _ in range(K):
        baechu_x, baechu_y = map(int, sys.stdin.readline().strip().split())
        baechu_pos[baechu_y][baechu_x] = 1

    checker = [[0 for _ in range(X)] for _ in range(Y)]
    queue = collections.deque()
    count = 0
# X부터 하나씩 배추밭을 탐색
    for i in range(Y):
        for j in range(X):
            if baechu_pos[i][j] == 0:
                checker[i][j] == 1
                continue
# 확인하지 않은 배추밭을 bfs로 탐색
            if checker[i][j] == 0:
                count += 1
                queue.append((i, j))
                while queue:
                    now_y, now_x = queue.popleft()
                    if checker[now_y][now_x] == 0:
                        checker[now_y][now_x] = 1

                        for k in range(4):
                            new_x = now_x + dx[k]
                            new_y = now_y + dy[k]

                            if 0 <= new_x < X and 0 <= new_y < Y and baechu_pos[new_y][new_x] == 1:
                                    checker[new_y][new_x] == 1
                                    queue.append((new_y, new_x))

    print(count)

