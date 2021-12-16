import sys
import itertools
read = sys.stdin.readline

N = int(read())


for i in itertools.permutations(range(1, N + 1), N):
    print(*i)
