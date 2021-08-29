import sys
# 공백을 추가해주어, string[0] = ' ' 이 되게 만들었다.
first_string = ' ' + sys.stdin.readline().strip()
second_string = ' ' + sys.stdin.readline().strip()

# 각 string의 길이를 저장해주고
first_len = len(first_string)
second_len = len(second_string)

# string의 길이만큼 2차원 배열을 만들었다. 이는 각 string의 길이일 때, LCS를 저장해두는 memo이다.
memo_table = [[0] * (second_len) for _ in range(first_len)]

# memo_table[i][j]는 새롭게 추가된 string이 같으면, memo[i - 1][j - 1] + 1과 같다. 그렇지 않다면, first_string이 한 개 짧을 때와 second_stirng이 한 개 짧을 때 중 큰 값을 가진다.
for i in range(1, first_len):
    first_new_str = first_string[i]
    for j in range(1, second_len):
        second_new_str = second_string[j]
        if first_new_str == second_new_str:
            memo_table[i][j] = memo_table[i - 1][j - 1] + 1
        else:
            memo_table[i][j] = max(memo_table[i][j - 1], memo_table[i - 1][j])



print(memo_table[first_len - 1][second_len - 1])