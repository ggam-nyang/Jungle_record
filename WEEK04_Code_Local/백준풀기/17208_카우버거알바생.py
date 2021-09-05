import sys
read = sys.stdin.readline


order_N, left_burger, left_fries = map(int, read().strip().split())
order_list = [[0, 0]] + [list(map(int, read().strip().split())) for _ in range(order_N)]

# 주문의 개수가 i개이고, 남은 버거는 bur, 남은 후라이는 fri일 때 처리할 수 있는 최대 주문의 수를 담는 dp배열
dp = [[[0] * (left_fries + 1) for _ in range(left_burger + 1)] for _ in range(order_N + 1)]


for i in range(1, len(order_list)):
    burger, fries = order_list[i]
# 현재 가진 햄버거와 후라이의 개수, 즉 bur / fri 가 요구량보다 넉넉하다면, 그 양을 뺐을 때 처리할 수 있는 주문의 수 + 1을 해준다.
    for bur in range(1, left_burger + 1):
        for fri in range(1, left_fries + 1):
            if burger <= bur and fries <= fri:
                dp[i][bur][fri] = max(1 + dp[i - 1][bur - burger][fri - fries], dp[i - 1][bur][fri])
            else:
                dp[i][bur][fri] = dp[i - 1][bur][fri]

answer = []
for i in dp:
    temp = list(map(max, i))
    answer.append(max(temp))
print(max(answer))


# print(dp[order_N][left_burger][left_fries]) 이렇게 출력하는게 더 효율적일듯!