import sys

prob = sys.stdin.readline().strip()

if prob[1] != 'x' and prob[0] == '0':
    print(int(prob, base=8))
elif prob[0] == '0':
    print(int(prob, base=16))
else:
    print(int(prob))

