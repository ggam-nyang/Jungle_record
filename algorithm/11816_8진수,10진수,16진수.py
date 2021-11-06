import sys

prob = sys.stdin.readline().strip()

if prob[1] != 'x' and prob[0] == '0':
    temp = ''.join(prob)
    print(int(temp, base=8))
elif prob[0] == '0':
    temp = ''.join(prob)
    print(int(temp, base=16))
else:
    print(int(prob))

