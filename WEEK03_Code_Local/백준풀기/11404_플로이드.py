import sys

city_n = int(sys.stdin.readline().strip())
bus_m = int(sys.stdin.readline().strip())
INF = int(1e9)

bus_route = [[INF] * (city_n + 1) for _ in range(city_n + 1)]

for i in range(1, city_n + 1):
    bus_route[i][i] = 0

for _ in range(bus_m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    bus_route[a][b] = min(bus_route[a][b], c)



def floid():
    for k in range(city_n + 1):
        for i in range(city_n + 1):
            for j in range(city_n + 1):
                if bus_route[i][k] and bus_route[k][j]:
                    bus_route[i][j] = min(bus_route[i][j], bus_route[i][k] + bus_route[k][j])


floid()
for i in range(1, city_n + 1):
    for j in range(1, city_n + 1):
        if bus_route[i][j] == INF:
            bus_route[i][j] = 0

for i in range(1, city_n + 1):
    print(*bus_route[i][1:])

