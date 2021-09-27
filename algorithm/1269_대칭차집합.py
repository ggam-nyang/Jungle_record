import sys
read = sys.stdin.readline

count_a, count_b = map(int, read().split())

a_group = list(map(int, read().split()))
b_group = list(map(int, read().split()))

a_group.sort()
b_group.sort()

a_index = 0
b_index = 0

answer = 0
while a_index < len(a_group) and b_index < len(b_group):
    if a_group[a_index] == b_group[b_index]:
        a_index += 1
        b_index += 1
    elif a_group[a_index] > b_group[b_index]:
        b_index += 1
        answer += 1
    else:
        a_index += 1
        answer += 1

while a_index < len(a_group):
    a_index += 1
    answer += 1

while b_index < len(b_group):
    b_index += 1
    answer += 1

print(answer)