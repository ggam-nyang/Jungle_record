import sys
import functools
read = sys.stdin.readline

matrix_N = int(read().strip())

matrix_list = []
for _ in range(matrix_N):
    row, col = map(int, read().strip().split())
    matrix_list.append((row, col))

dp = [[0] * (matrix_N) for _ in range(matrix_N)]


# @functools.lru_cache()
# def make_matrix_multiply(x, y):
#     if dp[x][y] != -1:
#         return dp[x][y]

#     if x == y:
#         return 0

#     if x + 1 == y:
#         return matrix_list[x][0] * matrix_list[x][1] * matrix_list[y][1]

#     for k in range(x, y):
#         left = make_matrix_multiply(x, k)
#         right = make_matrix_multiply(k + 1, y)
#         temp = left + right + matrix_list[x][0] * matrix_list[k][1] * matrix_list[y][1]

#         if dp[x][y] == -1 or dp[x][y] > temp:
#             dp[x][y] = temp
#     return dp[x][y]

# print(make_matrix_multiply(0, matrix_N - 1))


for x in range(1, matrix_N):
    for i in range(matrix_N - x):
        j = i + x
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1])
print(dp[0][matrix_N - 1])



