import sys
read = sys.stdin.readline


number = int(read().strip())
def make_divisor(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return i
    return num


while number > 1:
    temp = make_divisor(number)
    number //= temp
    print(temp)

