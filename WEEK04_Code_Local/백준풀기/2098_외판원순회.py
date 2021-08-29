import sys
read = sys.stdin.readline

city_N = int(read().strip())

cost_list = [list(map(int, read().strip().split())) for _ in range(city_N)]


city = []
for i in range(city_N):
    city.append(i)

ans = []

def get_shortest_dist(start, n, nums):
    global ans
    if not nums:
        return cost_list[n][start]


    temp = sys.maxsize
    for k in range(len(nums)):
        if cost_list[n][nums[k]] == 0:
            continue
        temp = min(temp, cost_list[n][nums[k]] + get_shortest_dist(start, nums[k], nums[:k] + nums[k + 1:]))

    return temp


temp = sys.maxsize
for i in range(city_N):
    temp = min(temp, get_shortest_dist(i, i, city[:i] + city[i + 1:]))

print(temp)