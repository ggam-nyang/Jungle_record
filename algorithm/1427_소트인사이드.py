import sys

N = sys.stdin.readline().strip()
num_arr = [0] * 10

for s in N:
    num_arr[int(s)] += 1

for i in range(9, -1, -1):
    for j in range(num_arr[i]):
        print(i, sep='', end='')

