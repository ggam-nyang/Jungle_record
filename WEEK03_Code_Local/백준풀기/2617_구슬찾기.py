import sys

bead_N, edge = map(int, sys.stdin.readline().strip().split())

# 나보다 무거운 구슬을 담아 놓은 리스트와 가벼운 구슬을 담아 놓는 리스트를 구분해서 만듦!
# dfs를 통해 나보다 무거운 or 가벼운 구슬이 몇개인지 파악하기 위함
heavy_bead_list = [[] for _ in range(bead_N + 1)]
light_bead_list = [[] for _ in range(bead_N + 1)]
for _ in range(edge):
    heavy, light = map(int, sys.stdin.readline().strip().split())
    heavy_bead_list[light].append(heavy)
    light_bead_list[heavy].append(light)

# 평범한 dfs, 계속 타고 가면 몇개의 node까지 탈 수 있는지 return 해줌
def dfs(node, list):
    global visited
    global check
    visited[node] = 1
    for bead in list[node]:
        if visited[bead] == 0:
            check += 1
            dfs(bead, list)



count = 0
md = (bead_N + 1) / 2
for i in range(1, bead_N + 1):
    visited = [0] * (bead_N + 1)

    check = 0
    dfs(i, heavy_bead_list)
    if (check >= md):
        count += 1

    check = 0
    dfs(i, light_bead_list)
    if check >= md:
        count += 1


print(count)