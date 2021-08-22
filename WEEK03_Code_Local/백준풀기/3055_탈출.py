import sys
import collections

R, C = map(int, sys.stdin.readline().strip().split())

tiddub_forest = []
for _ in range(R):
    tiddub_forest.append(list(sys.stdin.readline().strip()))

hedge = collections.deque()
water = collections.deque()

dx = [0 , 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = None


# 고슴도치의 처음 위치와 물의 처음 위치를 각각의 queue에 저장하고, 고슴도치를 숫자 1로 변환
for row in range(R):
    for col in range(C):
        if tiddub_forest[row][col] == '*':
            water.append((row, col))
        elif tiddub_forest[row][col] == 'S':
            tiddub_forest[row][col] = 1
            hedge.append((row, col))

# 고슴도치의 움직임을 보여주는 bfs 함수,  고슴도치가 먼저 움직이고, 'D'를 만나면 ans에 해당 최단거리를 저장한다.
def hedge_bfs(hx, hy):
    global ans
    for i in range(4):
        hx_new = hx + dx[i]
        hy_new = hy + dy[i]
        if 0 <= hx_new < R and 0 <= hy_new < C:
            if tiddub_forest[hx_new][hy_new] == '.':
                tiddub_forest[hx_new][hy_new] = tiddub_forest[hx][hy] + 1
                hedge.append((hx_new, hy_new))
            elif tiddub_forest[hx_new][hy_new] == 'D':
                ans = tiddub_forest[hx][hy]

# 물의 움직임을 보여주는 bfs 함수, 물이 나중에 움직이고 'D', '*', 'X'이 아니면(비버, 물, 돌) 모두 물로 바꾼다 (고슴도치가 잠길 위치에 있으면 잠겨서 물이 된다!)
def water_bfs(wx, wy):
    for i in range(4):
        wx_new = wx + dx[i]
        wy_new = wy + dy[i]
        if 0 <= wx_new < R and 0 <= wy_new < C:
            if tiddub_forest[wx_new][wy_new] == '.':
                tiddub_forest[wx_new][wy_new] = '*'
                water.append((wx_new, wy_new))
            elif tiddub_forest[wx_new][wy_new] != 'D' and tiddub_forest[wx_new][wy_new] != '*' and tiddub_forest[wx_new][wy_new] != 'X':
                tiddub_forest[wx_new][wy_new] = '*'
                water.append((wx_new, wy_new))
# 도치가 물에 잠기면, queue에 담겨 있던 그 위치의 도치를 제거한다! (도치가 잠기면 없어지니까)
                if (wx_new, wy_new) in hedge:
                    hedge.remove((wx_new, wy_new))


# 도치 - 물 - 도치 - 물  순으로 움직이기 위해, 각 queue의 저장된만큼만 움직인다.
while ans == None and hedge:
    for _ in range(len(hedge)):
        hedge_x, hedge_y = hedge.popleft()
        hedge_bfs(hedge_x, hedge_y)


    for _ in range(len(water)):
        water_x, water_y = water.popleft()
        water_bfs(water_x, water_y)


if ans == None:
    print('KAKTUS')
else:
    print(ans)