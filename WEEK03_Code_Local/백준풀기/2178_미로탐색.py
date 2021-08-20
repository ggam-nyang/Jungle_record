import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())

miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
## bfs를 사용해서 같은 계층?의 탐색에 숫자를 준다.





def bfs(miro_list, start):
    # 방문 체크 배열 visited, 방문할 곳 저장 need_visited, 각 위치의 최단거리 기록 way_map
    visited = [[0 for _ in range(M)] for _ in range(N)]
    need_visited = deque()
    way_map = [[0 for _ in range(M)] for _ in range(N)]
    way_map[0][0] = 1

    # 상하좌우 1인 길을 찾고 방문할 곳에 저장 및 거리를 기록하는 함수
    def find_way(x, y):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x <= N - 1 and 0 <= new_y <= M - 1 and miro_list[new_x][new_y] == 1:
                if visited[new_x][new_y] == 0:
                    need_visited.append((new_x, new_y))
                    visited[new_x][new_y] = 1
                    way_map[new_x][new_y] = way_map[x][y] + 1


    need_visited.append(start)
# 방문할 곳이 없을 때까지 반복!!
    while need_visited:
        now = need_visited.popleft()
        visited[now[0]][now[1]] = 1
        find_way(now[0], now[1])

    return way_map[N -1][M - 1]
print(bfs(miro, (0, 0)))

