import sys
read = sys.stdin.readline

sensor_N = int(read().strip())
station_N = int(read().strip())

if sensor_N <= station_N:
    print(0)
    exit(0)

sensor_list = list(map(int, read().strip().split()))
sensor_list.sort()


dist = []
for i in range(1, sensor_N):
    dist.append(sensor_list[i] - sensor_list[i - 1])
dist.sort()



for _ in range(station_N - 1):
    dist.pop()
print(sum(dist))