import sys

N = int(sys.stdin.readline().strip())

def fibo(num):
    fibo_arr = [0, 1]

    for i in range(2, num + 1):
        fibo_arr.append(fibo_arr[i - 1] + fibo_arr[i - 2])

    return fibo_arr[num]



print(fibo(N))
