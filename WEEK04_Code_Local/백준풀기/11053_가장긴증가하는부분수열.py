import sys
read = sys.stdin.readline

sequence_length = int(read().strip())

sequence_list = list(map(int, read().strip().split()))

def make_longest_sequence():
    dp = [0] * (sequence_length)
    for i in range(sequence_length):
        for j in range(i):
            if dp[i] < dp[j] and sequence_list[i] > sequence_list[j]:
                dp[i] = dp[j]
        dp[i] += 1
    return dp
print(max(make_longest_sequence()))