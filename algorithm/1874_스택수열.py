import sys
read = sys.stdin.readline

n = int(read())
answer = ['+']
stack = [1]
curr_num = 1
max_num = 0
temp_num = int(read())

while curr_num <= n and stack:


    if temp_num == stack[-1]:
        answer.append('-')
        stack.pop()

        if stack == []:
            stack.append(curr_num)
            continue
        if stack or curr_num <= n:
            temp_num = int(read())
        else:
            break

    elif temp_num < stack[-1]:
        answer.append('-')
        print("No")
        exit(0)
        curr_num -= 1

    else:
        answer.append('+')
        curr_num += 1
        stack.append(curr_num)

    print(answer, curr_num)
    print(stack)

print(answer)

