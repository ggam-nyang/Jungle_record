def solution(n, build_frame):
    global pil_graph, bo_graph
    answer = []

    pil_graph = [[0] * (n + 1) for _ in range(n + 1)]
    bo_graph = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(len(build_frame)):
        x, y, is_bo, is_install = build_frame[i]
        if is_install:
            if is_bo:
                if bo_install(x, y):
                    bo_graph[x][y] = 1
                    answer.append([x, y, 1])
            else:
                if pil_install(x, y):
                    pil_graph[x][y] = 1
                    answer.append([x, y, 0])
        else:
            if is_bo:
                if bo_remove(x, y):
                    answer.remove([x, y, 1])
            else:
                if pil_remove(x, y):
                    answer.remove([x, y, 0])
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer


def bo_install(x, y):
    if pil_graph[x][y - 1] == 1 or pil_graph[x + 1][y - 1]:
        return True
    if bo_graph[x - 1][y] == 1 and bo_graph[x + 1][y] == 1:
        return True

    return False

def pil_install(x, y):
    if y == 0:
        return True

    if pil_graph[x][y - 1] == 1:
        return True

    if bo_graph[x][y] == 1:
        return True

    if bo_graph[x - 1][y] == 1:
        return True

    return False

def bo_remove(x, y):
    bo_graph[x][y] = 0
    answer = True
    if bo_graph[x - 1][y] == 1:
        if not bo_install(x - 1, y):
            answer = False

    if bo_graph[x + 1][y] == 1:
        if not bo_install(x + 1, y):
            answer = False

    if pil_graph[x][y] == 1:
        if not pil_install(x, y):
            answer = False

    if pil_graph[x + 1][y] == 1:
        if not pil_install(x + 1, y):
            answer = False

    if not answer:
        bo_graph[x][y] = 1
        return answer

    return answer

def pil_remove(x, y):
    pil_graph[x][y] = 0
    answer = True
    if bo_graph[x][y + 1] == 1:
        if not bo_install(x, y + 1):
            answer = False

    if bo_graph[x - 1][y + 1] == 1:
        if not bo_install(x - 1, y + 1):
            answer = False

    if pil_graph[x][y + 1] == 1:
        if not pil_install(x, y + 1):
            answer = False

    if not answer:
        pil_graph[x][y] = 1
        return answer

    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1],[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
))