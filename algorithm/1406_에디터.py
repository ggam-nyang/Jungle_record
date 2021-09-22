import sys
read = sys.stdin.readline

first_stack = list(read().strip())
order_N = int(read().strip())
second_stack = []

def do_order(order):
    if order[0] == 'L':
        if first_stack:
            second_stack.append(first_stack.pop())
    elif order[0] == 'D':
        if second_stack:
            first_stack.append(second_stack.pop())
    elif order[0] == 'B':
        if first_stack:
            first_stack.pop()
    else:
        first_stack.append(order[1])


for i in range(order_N):
    now_order = read().strip().split()
    do_order(now_order)

print(*first_stack, sep='', end='')
print(*reversed(second_stack), sep='', end='')
