import sys
read = sys.stdin.readline

sanggeun_card_N = int(read().strip())
card_list = list(map(int, read().strip().split()))

number_N = int(read().strip())
number_list = list(map(int, read().strip().split()))

is_sanggeun_own = [0] * number_N

card_list.sort()


for i in range(len(number_list)):
    left_index = 0
    right_index = len(card_list) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if card_list[mid_index] < number_list[i]:
            left_index = mid_index + 1
        elif card_list[mid_index] > number_list[i]:
            right_index = mid_index - 1
        else:
            is_sanggeun_own[i] = 1
            break
print(*is_sanggeun_own)
