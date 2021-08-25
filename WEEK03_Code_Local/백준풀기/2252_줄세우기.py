import sys

N, M = map(int, sys.stdin.readline().strip().split())

height_list = [[] for _ in range(N + 1)]

# 2차원 배열에  a < b임을 저장하기
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    height_list[a].append(b)



visited = [0] * (N + 1)

sorting_box = []
# 마지막 줄이 핵심! 다 방문하고 나서 list에 추가해준다. 재귀이기 때문에, 가장 마지막 호출된 함수가 먼저 담긴다! 1 2 3호출하면 [3, 2, 1]이 담긴다
def dfs(x):
    visited[x] = 1

    for target in height_list[x]:
        if visited[target] == 0:
            visited[target] = 1
            dfs(target)
    sorting_box.append(x)


for i in range(N + 1):
    if visited[i] == 0 and len(height_list[i]):
        dfs(i)

# 아무것도 연결되지 않은 노드를 추가하기 위함. (굉장히 비효율적인듯)
for i in range(1, N + 1):
    if len(height_list[i]) == 0 and i not in sorting_box:
        sorting_box.append(i)

print(*sorting_box[::-1])