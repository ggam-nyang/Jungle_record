import sys
read = sys.stdin.readline

length, width, height = map(int, read().strip().split())
cube_N = int(read())
cube_list = []
for _ in range(cube_N):
    cube_kind, cube_count = map(int, read().split())
    cube_list.append(cube_count)


