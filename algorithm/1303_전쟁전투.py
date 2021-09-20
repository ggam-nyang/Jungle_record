import sys
read = sys.stdin.readline

M, N = map(int, read().strip().split())
battle_ground = [list(read().strip()) for _ in range(N)]
checker = [[0] * M for _ in range(N)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

white_sum = 0
blue_sum = 0

white_count = 1
blue_count = 1
def find_team(x, y, team):
    global white_count, blue_count
    checker[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and battle_ground[nx][ny] == team:
            if checker[nx][ny] == 0:
                if team == 'B':
                    blue_count += 1
                else:
                    white_count += 1
                find_team(nx, ny, team)
for i in range(N):
    for j in range(M):
        if checker[i][j] == 0:
            white_count, blue_count = 1, 1
            find_team(i, j, battle_ground[i][j])
            if battle_ground[i][j] == 'W':
                white_sum += white_count ** 2
            else:
                blue_sum += blue_count ** 2

print(white_sum, blue_sum)