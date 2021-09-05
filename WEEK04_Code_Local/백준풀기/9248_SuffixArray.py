import sys



S = sys.stdin.readline().strip()
N = len(S)


suffix_array = []
for i in range(N):
    suffix_array.append(S[i:])

