from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    answer_list = []
    for user_list in permutations(user_id, len(banned_id)):

        flag = False
        for i in range(len(banned_id)):
            if not check_id(user_list[i], banned_id[i]):
                # print(user_list[i], banned_id[i])
                flag = True
                break
        if flag:
            continue
        users = sorted(user_list)
        if users not in answer_list:
            answer_list.append(users)

    answer = len(answer_list)
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