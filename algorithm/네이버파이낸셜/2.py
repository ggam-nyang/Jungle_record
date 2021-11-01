def solution(n, jump):
    answer = []

    a, b = find_cordinate(n, jump)

    answer = [a, b]

    return answer


def find_cordinate(n, jump):
    graph = [[0] * n for _ in range(n)]
    graph[0][0] = 1

    checker = [[0] * n for _ in range(n)]
    checker[0][0] = 1

    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    numbering = 2
    count = 0

    while numbering < n * n:
        new_x = x + dx[direction]
        new_y = y + dy[direction]



        if graph[new_x][new_y] == 0:
            count += 1
            if count % jump == 0:
                graph[new_x][new_y] = numbering
                numbering += 1

        if new_x >= n - 1 or new_x <= 0 or new_y >= n - 1 or new_y <= 0 or checker[new_x + dx[direction]][new_y + dx[direction]] == 1:
            direction = (direction + 1) % 4

        checker[new_x][new_y] = 1
        x = new_x
        y = new_y

        if (count + 1) % (n ** 2) == 0:
            x, y = 0, 0
            direction = 0
            checker = [[0] * n for _ in range(n)]
            checker[0][0] = 1
        print(x, y, count, numbering)
    return (x, y)


print(solution(3, 10))