import sys
read = sys.stdin.readline

N = read().strip()
numbers = int(read())

def sum_digits(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10
    return ans

print(sum_digits(numbers))