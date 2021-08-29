import sys

coin_N, K = map(int, sys.stdin.readline().strip().split())
coin_list = []

for _ in range(coin_N):
    coin = int(sys.stdin.readline().strip())
    coin_list.append(coin)

# 필요한 코인의 개수를 세주는 함수
# 가장 큰 코인으로 나누어 떨어진다면, 가장 가치가 큰 코인으로 최대한 빼준다! (Greedy 알고리즘)
def get_coin_count(list, cost):
    count = 0
    for i in range(len(list) - 1, -1, -1):
        if cost // list[i] > 0:
            count += cost // list[i]
            cost = cost % list[i]
        if cost == 0:
            break
    return count

print(get_coin_count(coin_list, K))