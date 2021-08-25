import sys
import collections


N, M = map(int, sys.stdin.readline().strip().split())

height_list = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
queue = collections.deque()


for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    height_list[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)


sorting_box = []
while queue:
    target = queue.popleft()
    sorting_box.append(target)
    for i in height_list[target]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
print(*sorting_box)
