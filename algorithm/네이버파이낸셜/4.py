def solution(board):
    answer = 0
    global score_list
    score_list = []
    score = board[0][0]
    N = len(board)

    stack = [(0, 0, score)]
    while stack:
        x, y, now_score = stack.pop()
        if x == N - 1 and y == N - 1:
            score_list.append(now_score)

        if x + 1 < N:
            if (board[x + 1][y] == 0):
                stack.append((x + 1, y, now_score))
                stack.append((x + 1, y, -now_score))
            else:
                stack.append((x + 1, y, now_score + board[x + 1][y]))

        if y + 1 < N:
            if (board[x][y + 1] == 0):
                stack.append((x, y + 1, now_score))
                stack.append((x, y + 1, -now_score))
            else:
                stack.append((x, y + 1, now_score + board[x][y + 1]))
    answer = max(score_list)
    return answer

