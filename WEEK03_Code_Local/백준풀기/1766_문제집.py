import sys

problem_N, problem_info = map(int, sys.stdin.readline().strip().split())

problems = [[] for _ in range(problem_N + 1)]
indegree = [0] * (problem_N + 1)
queue = []

# 간선들을 받아주고, indegree를 표시해준다.
for _ in range(problem_info):
    a, b = map(int, sys.stdin.readline().strip().split())
    problems[a].append(b)
    indegree[b] += 1


for i in range(1, problem_N + 1):
    if indegree[i] == 0:
        queue.append(i)

problem_procedure = []


# sort가 너무 비효율적이다. heapq를 이용했으면 훨씬 좋았을 듯.
while queue:
    queue.sort()

    start_node = queue[0]
    del queue[0]
    problem_procedure.append(start_node)

    for node in problems[start_node]:
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)

print(*problem_procedure)