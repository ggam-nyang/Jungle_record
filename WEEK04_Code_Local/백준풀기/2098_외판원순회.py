import sys
read = sys.stdin.readline

city_N = int(read().strip())

cost_list = [list(map(int, read().strip().split())) for _ in range(city_N)]

DP = [[-1] * (1 << city_N) for _ in range(city_N)]
def tsp(start, visited):
    VISITED_ALL = (1 << city_N) - 1

    if visited == VISITED_ALL:
        if not cost_list[start][0] == 0:
            return cost_list[start][0]
        else:
            return sys.maxsize
    if not DP[start][visited] == -1:
        return DP[start][visited]

    cost = sys.maxsize
    for city in range(city_N):
        if not visited & (1 << city) == 0:
            continue
        if cost_list[start][city] == 0:
            continue
        cost = min(cost, tsp(city, visited | (1 << city)) + cost_list[start][city])
    DP[start][visited] = cost

    return cost

print(tsp(0, 1))
