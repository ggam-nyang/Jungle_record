import sys

length_N = int(sys.stdin.readline())
num_list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

hidden_string = sys.stdin.readline().strip()
stack = []

answer = 0
temp = ''

for s in hidden_string:
    if s in num_list:
        temp += s
    else:
        if temp != '':
            answer += int(temp)
            temp = ''
if temp != '':
    answer += int(temp)


print(answer)
