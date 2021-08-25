import sys
sys.setrecursionlimit(1000000)


node_N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(node_N + 1)]

for _ in range(node_N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (node_N)
def dfs(x, parent):
    for node in graph[x]:
        if node != parent:
            idx = graph[x].index(node)
            graph[x][idx] = -1
            dfs(node, x)

dfs(1, None)
for i in range(2, node_N + 1):
    for j in graph[i]:
        if j != -1:
            print(j)

