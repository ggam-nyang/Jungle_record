import sys
read = sys.stdin.readline

str_list = list(map(str, read().strip()))

n = len(str_list)
zero = str_list.count('0') // 2
one = str_list.count('1') // 2

for i in range(zero):
    str_list.pop(-str_list[::-1].index('0') - 1)

for i in range(one):
    str_list.pop(str_list.index('1'))

print(''.join(str_list))

