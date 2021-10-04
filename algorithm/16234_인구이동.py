import sys
read = sys.stdin.readline
import collections



size_N, L, R = map(int, read().strip().split())
population_map = [list(map(int, read().strip().split())) for _ in range(size_N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_least_one_open(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < size_N and 0 <= ny < size_N and L <= abs(population_map[x][y] - population_map[nx][ny]) <= R:
            if checker_is_open[nx][ny] == 0:
                checker_is_open[x][y] = 1
                return True



def make_union_population(x, y):
    temp_union = [(x, y)]
    count_union = 1
    count_population = population_map[x][y]
    queue = collections.deque()
    queue.appendleft((x, y))

    while queue:
        p, q = queue.popleft()
        for i in range(4):
            nx = p + dx[i]
            ny = q + dy[i]
            if 0 <= nx < size_N and 0 <= ny < size_N and L <= abs(population_map[p][q] - population_map[nx][ny]) <= R:
                if checker_is_open[nx][ny] == 0:
                    checker_is_open[nx][ny] = 1
                    queue.appendleft((nx, ny))
                    count_union += 1
                    count_population += population_map[nx][ny]
                    temp_union.append((nx, ny))
    union_population = count_population // count_union
    for union in temp_union:
        population_map[union[0]][union[1]] = union_population

def is_not_finish(graph):
    for i in range(size_N):
        for j in range(size_N):
            if graph[i][j] == 1:
                return True
    return False



move_day = 0
checker = [[0] * size_N for _ in range(size_N)]
is_not_finished = True


while is_not_finished:
    checker_is_open = [[0] * size_N for _ in range(size_N)]
    for r in range(size_N):
        for c in range(size_N):
            if checker_is_open[r][c] == 0 and check_least_one_open(r, c):
                make_union_population(r, c)
                is_not_finished = False
    if is_not_finished == True:
        break
    move_day += 1
    is_not_finished = is_not_finish(checker_is_open)
print(move_day)
