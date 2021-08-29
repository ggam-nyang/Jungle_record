import sys

N = int(sys.stdin.readline().strip())

def find_sequence_N(num):
    prev1 = 1
    prev2 = 2
    if num == 1:
        return prev1
    elif num == 2:
        return prev2

    for i in range(num - 2):
        current = (prev1 + prev2) % 15746
        prev1, prev2 = prev2, current

    return current
print(find_sequence_N(N))