import sys
read = sys.stdin.readline

sequence_length = int(read().strip())

sequence_list = list(map(int, read().strip().split()))

def make_longest_sequence():
    max_dp = 1
    ans = [[sequence_list[0]]]
    dp = [0] * (sequence_length)
    for i in range(sequence_length):
        for j in range(i):
            if dp[i] < dp[j] and sequence_list[i] > sequence_list[j]:
                dp[i] = dp[j]
        dp[i] += 1

        if max_dp < dp[i]:
            ans.append(ans[-1] + [sequence_list[i]])
            max_dp = dp[i]
        elif max_dp >= dp[i]:
            ans[dp[i] -1] = ans[dp[i] - 2][:dp[i]] + [sequence_list[i]]

    return ans

answer = make_longest_sequence()[-1][1:]
print(len(answer))
print(*answer)




# print(len(ans))
# print(*ans)