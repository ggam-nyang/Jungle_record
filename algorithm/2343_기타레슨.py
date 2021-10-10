import sys
read = sys.stdin.readline

lecture_N, blueray_M = map(int, read().strip().split())
lecture_list = list(map(int, read().split()))

def is_blueray_divided(size):
    temp_sum = 0
    count = 0
    for i in range(len(lecture_list)):
        if temp_sum + lecture_list[i] > size:
            count += 1
            temp_sum = 0

        temp_sum += lecture_list[i]
    else:
        if temp_sum:
            count += 1
    return count

left = max(lecture_list)
right = sum(lecture_list)

answer = left

while left <= right:
    mid = (left + right) // 2
    count_br = is_blueray_divided(mid)
    if (count_br > blueray_M):
        left = mid + 1
    else:
        # if count_br == blueray_M:
        #     answer = mid
        right = mid - 1

print(left)


