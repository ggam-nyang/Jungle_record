def check_string(strings):
    number_array_for_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for s in strings:
        if s not in number_array_for_check:
            return False
    return True


def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = check_string(s)

    return answer


