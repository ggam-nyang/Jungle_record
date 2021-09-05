import sys
import collections
read = sys.stdin.readline


# 입력값 받기
children_N, relationship_N, resonance = map(int, read().strip().split())

candy_list = [0] + list(map(int, read().strip().split()))
friend_list = [[] for _ in range(children_N + 1)]
for _ in range(relationship_N):
    a, b = map(int, read().strip().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

# 연결된 친구의 group을 구하기 위한 함수
visited = [0] * (children_N + 1)
def bfs(x):
    group = [[x], candy_list[x]]
    queue = collections.deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        now_x = queue.popleft()

        for i in range(len(friend_list[now_x])):
            if visited[friend_list[now_x][i]] == 0:
                friend = friend_list[now_x][i]
                visited[friend] = 1
                queue.append(friend)
                group[0].append(friend)
                group[1] += candy_list[friend]

    return group


# 연결된 친구들의 그룹을 표시함. [[연결된 친구 번호들], 총 candy 수] 로 표현함
children_group = []
for i in range(1, children_N + 1):
    if visited[i] == 0:
        children_group.append(bfs(i))
children_group = [0] + children_group

dp = [[0] * (resonance + 1) for _ in range(len(children_group))]

# 배낭 문제와 동일한 로직으로 해결!!
for i in range(1, len(children_group)):
    children, candy = len(children_group[i][0]), children_group[i][1]
    for reso in range(1, resonance + 1):
        if reso <= children:
            dp[i][reso] = dp[i - 1][reso]
        else:
            dp[i][reso] = max(dp[i - 1][reso - children] + children_group[i][1], dp[i - 1][reso])

print(dp[len(children_group) - 1][resonance])

