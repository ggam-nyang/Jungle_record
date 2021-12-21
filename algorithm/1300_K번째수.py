import sys
read = sys.stdin.readline

N = int(read())
k = int(read())


def check_order_of_number(num):
    temp = 0
    for i in range(1, N + 1):
        temp += min(N, num // i)

    return temp

start = 1
end = pow(N, 2)

answer = 0


while start <= end:
    mid = (start + end) // 2
    count_below_mid = check_order_of_number(mid)

    if count_below_mid < k:
        start = mid + 1
    elif count_below_mid >= k:
        answer = mid
        end = mid - 1

print(answer)
