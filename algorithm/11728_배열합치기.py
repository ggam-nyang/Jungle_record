import sys
read = sys.stdin.readline

size_A, size_B = map(int, read().split())

list_A = list(map(int, read().split()))
list_B = list(map(int, read().split()))

a_index = 0
b_index = 0

answer = []

while a_index < len(list_A) and b_index < len(list_B):
    if list_A[a_index] <= list_B[b_index]:
        answer.append(list_A[a_index])
        a_index += 1
    else:
        answer.append(list_B[b_index])
        b_index += 1

while a_index < len(list_A):
    answer.append(list_A[a_index])
    a_index += 1

while b_index < len(list_B):
    answer.append(list_B[b_index])
    b_index += 1

print(*answer)

