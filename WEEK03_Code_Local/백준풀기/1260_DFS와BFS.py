import collections
import sys

N, M, V = map(int, sys.stdin.readline().strip().split())

connect_list = []
for _ in range(N + 1):
    connect_list.append([])

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if b not in connect_list[a]:
        connect_list[a].append(b)
    if a not in connect_list[b]:
        connect_list[b].append(a)
for i in range(N):
    connect_list[i + 1].sort()


# def dfs(list, start):
#     visited = []
#     stack = []
#     answer = []
#     stack.append(start)

#     while stack:
#         now = stack.pop()
#         if now not in visited:
#             visited.append(now)
#             answer.append(now)
#         for route in list[now][::-1]:
#             if route not in visited:
#                 stack.append(route)



    # return answer

def dfs(graph, start):
    need_visited, visited = [], []
    need_visited.append(start)

    while need_visited:
        now = need_visited.pop()
        if now not in visited:
            visited.append(now)
            need_visited.extend(graph[now][::-1])

    return visited


def dfs_recursive(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited



def bfs(list, start):
    visited = []
    queue = collections.deque()
    answer = []
    queue.append(start)

    while queue:
        now = queue.popleft()
        answer.append(now)
        if now not in visited:
            visited.append(now)
        for route in list[now]:
            if route not in visited:
                visited.append(route)
                queue.append(route)

    return answer



print(*dfs(connect_list, V))
print(*bfs(connect_list, V))
