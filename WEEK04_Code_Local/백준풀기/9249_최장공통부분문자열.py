import sys
read = sys.stdin.readline



A = read().strip()
B = read().strip()


def hash_function(str):
    ans = 0
    n = len(str)
    for i in range(n):
        ans += (ord(str[i]) - 96) * (26 ** (n - 1 - i))

    return ans

def hash_check(long, hash, n):
    temp = hash_function(long[:n])
    if temp == hash:
        return True
    for i in range(len(long) - n):
        if hash != temp:
            temp -= (ord(long[i]) - 96) * (26 ** (n - 1))
            temp = temp * 26 + (ord(long[i + n]) - 96)
        else:
            return True

    return False


answer = ''
if len(A) < len(B):
    short = A
    long = B
else:
    short = B
    long = A


for i in range(len(short) // 2 + 1):
    # print(short[i:])
    # print(short[:-i])
    if hash_check(long, hash_function(short[i:]), len(short) - i):
        answer = short[i:]
        break
    if hash_check(long, hash_function(short[:-i]), len(short) - i):
        answer = short[:-i]
        break


print(len(answer))
print(answer)





# 96을 빼자 ord에서