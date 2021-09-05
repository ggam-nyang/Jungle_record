# https://www.acmicpc.net/problem/2579
# 계단오르기

import sys
import functools
read = sys.stdin.readline

stairs_N = int(read().strip())
stair_point = [0] + [int(read().strip()) for _ in range(stairs_N)]


@functools.lru_cache()
def count_point(n):
    if n == 1:
        return stair_point[1]

    if n == 2:
        return stair_point[1] + stair_point[2]

    if n == 3:
        return max(stair_point[1] + stair_point[3], stair_point[2] + stair_point[3])



    return max(count_point(n - 2) + stair_point[n], count_point(n - 3) + stair_point[n - 1] + stair_point[n])


print(count_point(stairs_N))

