import sys

read = sys.stdin.readline

while True:
    num1, num2 = map(int, read().split())

    if (num1 == 0 and num2 == 0):
        break

    if num1 > num2:
        if num1 % num2 == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if num2 % num1 == 0:
            print("factor")
        else:
            print("neither")


