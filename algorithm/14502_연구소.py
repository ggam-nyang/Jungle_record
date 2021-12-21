import sys
import collections, itertools, copy
read = sys.stdin.readline

row_N, col_N = map(int, read().strip().split())
virus_graph = []

for _ in range(row_N):
    virus_graph.append(list(map(int, read().strip().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def make_three_wall(row, col):
    temp_list = []
    for i in range(row):
        for j in range(col):
            temp_list.append((i, j))

    return temp_list


def cal_safe_area(graph, row, col):
    visited = [[0] * col for _ in range(row)]
    virus_queue = collections.deque()


    for i in range(row):
        for j in range(col):
            if graph[i][j] == 2 and visited[i][j] == 0:
                visited[i][j] = 1
                virus_queue.append((i, j))

                while virus_queue:
                    x, y = virus_queue.popleft()

                    for k in range(4):
                        new_x = x + dx[k]
                        new_y = y + dy[k]

                        if 0 <= new_x < row and 0 <= new_y < col and graph[new_x][new_y] == 0:
                            if visited[new_x][new_y] == 0:
                                graph[new_x][new_y] = 2
                                visited[new_x][new_y] = 1
                                virus_queue.append((new_x, new_y))


    # if counting_safe_area(graph, row, col) > 3:
    #     print(graph)

    return counting_safe_area(graph, row, col)


def counting_safe_area(graph, row, col):
    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0:
                count += 1

    return count


answer_list= []
for walls in itertools.combinations(make_three_wall(row_N, col_N), 3):
    check_walls = False
    for wall in walls:
        if virus_graph[wall[0]][wall[1]] != 0:
            check_walls = True
            break

    if check_walls:
        continue
    temp_graph = copy.deepcopy(virus_graph)


    for wall in walls:
        temp_graph[wall[0]][wall[1]] = 1

    temp_answer = cal_safe_area(temp_graph, row_N, col_N)
    answer_list.append(temp_answer)

    for wall in walls:
        temp_graph[wall[0]][wall[1]] = 0


# print(cal_safe_area(virus_graph, row_N, col_N))

print(max(answer_list))
