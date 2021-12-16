import sys
read = sys.stdin.readline

N = int(read())

flag = False
answer = 0
temp_sum = 0
for i in range(1, N):
    answer = i
    temp_sum += i
    while i > 0:
        temp_sum += i % 10
        i //= 10
    if temp_sum == N:
        flag = True
        break
    temp_sum = 0

if flag == True:
    print(answer)
else:
    print(0)
