import sys
read = sys.stdin.readline

initial_string = read().strip()
bomb_string = read().strip()

bomb_len = len(bomb_string)

main_stack = []
bomb_point = 0

for string in initial_string:
    main_stack.append(string)
    if len(main_stack) >= bomb_len:
        if bomb_string == ''.join(main_stack[bomb_point:bomb_point + bomb_len]):
            for _ in range(bomb_len):
                main_stack.pop()
    bomb_point = len(main_stack) - bomb_len + 1
if main_stack:
    print(''.join(main_stack))
else:
    print('FRULA')
