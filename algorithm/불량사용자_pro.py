import operator as op
from functools import reduce

def solution(user_id, banned_id):
    answer = 1

    guess_banned_id = [[] for _ in range(9)]
    count_banned_len = [0] * 9
    count_correct_id = [0] * len(banned_id)
    i = 0
    flag = False
    for bann in banned_id:
        for user in user_id:
            if check_id(user, bann):
                user_len = len(user)
                if user not in guess_banned_id[user_len]:
                    guess_banned_id[user_len].append(user)
                    flag = True


        if flag:
            count_banned_len[user_len] += 1
        i += 1


    for i in range (9):
        if count_banned_len[i] != 0:
            answer *= nCr(len(guess_banned_id[i]), count_banned_len[i])

    return answer

def check_id(user_id, banned_id):
    user_len = len(user_id)
    bann_len = len(banned_id)
    if user_len != bann_len:
        return False

    for digit in range(user_len):
        if (banned_id[digit] == '*'):
            continue

        if (user_id[digit] != banned_id[digit]):
            return False
    return True

def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError

    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n - r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator // denominator
