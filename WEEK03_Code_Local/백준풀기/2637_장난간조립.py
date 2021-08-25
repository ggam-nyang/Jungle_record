import sys
import collections



parts_N = int(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())
# 부품간의 관계를 나타내기 위한 parts_need, 진입 차수를 표시하는 indegree
parts_need = [[0] * (parts_N + 1) for _ in range(parts_N + 1)]
indegree = [0] * (parts_N + 1)

# 해당 부품이, 어떤 중간 제품의 부품이 되는지 기록한다. ex 5 2 2 라면 2번 부품은 5번에게 2개 필요하므로 2번 부품의 인접행렬에 5번 인덱스에 2를 넣는다.
# parts_need[2][5] = 2, parts_need[part][target] = count
for _ in range(M):
    target, part, count = map(int, sys.stdin.readline().strip().split())
    parts_need[part][target] = count
    indegree[target] += 1


# basic_part에는 기본 부품을 넣는다 ( 초기에 진입차수가 0인 부품들 )
queue = collections.deque()
basic_part = []
for i in range(1, parts_N + 1):
    if indegree[i] == 0:
        queue.append(i)
        basic_part.append(i)
# 기본부품이 인접행렬의 본인 인덱스에 1개를 넣어준다. 이유는 while문에서 등장한다.
for basic in basic_part:
    parts_need[basic][basic] = 1



while queue:
    start = queue.popleft()
# 진입차수가 0인 경우에, 현재 부품이 어떤 부품의 재료인지 나와있다. 이를 읽고, target 부품에 현재 부품의 재료들을 추가해줘야한다.
## 이때 기본 부품들의 경우에는, 기본부품을 구성하는 재료 부품이 전부 0 이므로, 본인 자신은 1로 표시하여 부품을 추가할 수 있게한다.
    for i in range(1, parts_N + 1):
        if parts_need[start][i] > 0 and indegree[i] > 0:
            for basic in basic_part:
                parts_need[i][basic] += parts_need[start][basic] * parts_need[start][i]
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

for basic in basic_part:
    print(basic, parts_need[parts_N][basic])


