import sys

item_N, weight_limit = map(int, sys.stdin.readline().strip().split())

# 무게가 0이면, 가치도 0인 경우를 만들어둔다.
item_list = [(0, 0)]
for _ in range(item_N):
    weight, value = map(int, sys.stdin.readline().strip().split())
    item_list.append((weight, value))

## 정렬하지 않아도 되는지??

memo_list = [[0] * (weight_limit + 1) for _ in range(len(item_list))]

# 작은 무게부터 memo 하는데, 새로 담는 물건을 담을만큼 무게가 커지면 이 물건이 없을 때의 가치와 이 물건을 추가한 가치와 비교한다.
for i in range(1, item_N + 1):
    now_weight = item_list[i][0]
    now_value = item_list[i][1]
    for j in range(1, weight_limit + 1):
        if j < now_weight:
            memo_list[i][j] = memo_list[i - 1][j]
        else:
            memo_list[i][j] = max(now_value + memo_list[i - 1][j - now_weight], memo_list[i - 1][j])

max_v = 0

# for i in range(1, item_N + 1):
#     max_v = max(max_v, memo_list[i][weight_limit])


print(memo_list[item_N][weight_limit])



## 훨씬 빠른, dict를 이용한 방법
import sys

item_N, weight_limit = map(int, sys.stdin.readline().strip().split())
item_list = []

for _ in range(item_N):
    weight, value = map(int, sys.stdin.readline().strip().split())
    item_list.append((weight, value))

def backpack(n, k):
    dp = {0: 0}
    for i in range(n):
        new_w, new_v = item_list[i][0], item_list[i][1]
        temp = {}
        for acc_w, acc_v in dp.items():
            if acc_w + new_w <= k and acc_v + new_v > dp.get(acc_w + new_w, 0):
                temp[acc_w + new_w] = acc_v + new_v
        dp.update(temp)
    return max(dp.values())

print(backpack(item_N, weight_limit))







