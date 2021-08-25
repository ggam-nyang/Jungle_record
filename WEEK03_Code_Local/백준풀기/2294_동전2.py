import sys
import collections

n, k = map(int, sys.stdin.readline().strip().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(sys.stdin.readline().strip()))

coin_list.sort()

# (더해진 코인의 값, 더한 코인의 개수)를 저장할 queue 생성!
queue = collections.deque()
for coin in coin_list:
    queue.append((coin, 1))

# 코인의 값을 방문했다고 체크하기 위한 visited (예를 들어, 5는 (5, 1)도 가능하고 1코인 5개로 (5, 5)도 가능하다. 이를 막기 위해 visited 사용!)
visited = [0] * 10001
max_coin = max(coin_list)
min_count = 10001
while queue:
    now_coin, count = queue.popleft()

    for i in range(n):
        new_coin = now_coin + coin_list[i]

        # 더해진 코인의 값이 목표인 k보다 크다면 반복문 stop!
        if new_coin > k:
            break

        # queue에서 일찍 나오는 값이 count가 작다. 때문에 visited에 기록해두고 같은 값을 가질 때는 queue에 저장하지 않는다.
        if visited[new_coin] == 1:
            continue

        # 더해진 코인의 값이 목표인 k보다 작고, 현재 최소 coin의 개수인 min_count 보다 작다면 queue에 넣는다!
        if new_coin < k and count + 1 < min_count:
            visited[new_coin] = 1
            queue.append((new_coin, count + 1))
        elif new_coin == k:
            min_count = min(min_count, count + 1)

if min_count == 10001:
    min_count = -1
print(min_count)


# coin_list.sort(reverse=True)


# count_list = []
# def dfs(cost, count):
#     for coin in coin_list:
#         if cost == 0:
#             count_list.append(count)
#         elif cost // coin > 0:
#             dfs(cost % coin, count + cost // coin)



# dfs(k, 0)

# if count_list:
#     # print(count_list)
#     print(min(count_list))
# else:
#     print(-1)