def solution(s):
    answer = 0

    rotation_list = make_rotation_list(s)
    for i in range(len(s)):
        if check_bracket(rotation_list[i]):
            answer += 1

    return answer



def check_bracket(s):
    test_stack = []

    for i in s:
        if i == '(' or i == '{' or i == '[':
            test_stack.append(i)
        else:
            if not test_stack:
                return False


            if i == ')':
                if test_stack.pop() != '(':
                    return False
            elif i == '}':
                if test_stack.pop() != '{':
                    return False
            elif i == ']':
                if test_stack.pop() != '[':
                    return False
    if test_stack:
        return False

    return True

def make_rotation_list(s):
    return [s[x:] + s[:x] for x in range(len(s))]
