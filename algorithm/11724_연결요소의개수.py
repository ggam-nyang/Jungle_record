import sys, collections
read = sys.stdin.readline

sys.setrecursionlimit(10000)

point, edge = map(int, read().strip().split())
graph = [[0] * (point + 1) for _ in range(point + 1)]
visted = [0] * (point + 1)
count = 0
queue = collections.deque()



for _ in range(edge):
    point1, point2 = map(int, read().strip().split())
    graph[point1][point2] = 1
    graph[point2][point1] = 1

def dfs(p):

    for next in range(1, point + 1):
        if graph[p][next] == 1 and visted[next] == 0:
            visted[next] = 1
            dfs(next)

for i in range(1, point + 1):
    if visted[i] == 0:
        visted[i] = 1
        dfs(i)
        count += 1

print(count)

