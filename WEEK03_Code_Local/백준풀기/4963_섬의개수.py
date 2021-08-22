import sys

sys.setrecursionlimit(1000000000)



dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

def dfs(map_list, x, y):
    # visited 체크

    for i in range(8):
         new_x = x + dx[i]
         new_y = y + dy[i]

         if 0 <= new_x < h and 0 <= new_y < w and now_map[new_x][new_y] == 1:
             now_map[new_x][new_y] = 0
             dfs(map_list, new_x, new_y)



count_box = []

while True:
    w, h = map(int, sys.stdin.readline().strip().split())
    now_map = []
    count = 0

    for _ in range(h):
        now_map.append(list(map(int, sys.stdin.readline().strip().split())))

    if (w, h) == (0, 0):
        break



    for i in range(h):
        for j in range(w):
            if now_map[i][j] == 1:
                dfs(now_map, i, j)
                count += 1
    count_box.append(count)

for c in count_box:
    print(c)

