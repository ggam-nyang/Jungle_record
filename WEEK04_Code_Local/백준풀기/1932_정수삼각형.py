import sys
read = sys.stdin.readline

triangle_size = int(read().strip())
triangle_list = []
for _ in range(triangle_size):
    triangle_list.append(list(map(int, read().strip().split())))

dp = [0] * triangle_size
for i in range(triangle_size):
    temp = dp[::]
    for j in range(i + 1):
        dp[j] = triangle_list[i][j] + (temp[j] if j == 0 else max(temp[j], temp[j - 1]))

print(max(dp))
