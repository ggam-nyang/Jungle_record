import sys
import collections
singer_N, subpd_N = map(int, sys.stdin.readline().strip().split())

singer_order = [[] for _ in range(singer_N + 1)]
indegree = [0] * (singer_N + 1)

queue = collections.deque()

# 보조 pd들의 순서를 singer_order이라는 전체 2차원 배열에 저장.
for _ in range(subpd_N):
    sub_order = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, sub_order[0]):
        singer_order[sub_order[i]].append(sub_order[i + 1])
        indegree[sub_order[i + 1]] += 1


for i in range(1, singer_N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 일반적인 위상정렬 방식. 진입차수가 0인 노드를 제거하고, 그 노드와 연결된 노드들의 진입차수를 1씩 낮춘다. 그리고 다시 진입차수가 0이 된 노드를 queue에 추가한다.
fixed_order = []
while queue:
    start_node = queue.popleft()
    fixed_order.append(start_node)

    for node in singer_order[start_node]:
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)

# 가수의 수만큼 fixed_order에 담기지 않았다면, 싸이클이 생기는 부분이 생기는 것! 때문에 0 출력!
if len(fixed_order) != singer_N:
    print(0)
else:
    for singer in fixed_order:
        print(singer)
