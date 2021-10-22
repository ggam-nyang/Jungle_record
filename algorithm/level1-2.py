






def solution(answers):
    answer = []
    a_student = [1, 2, 3, 4, 5]
    b_student = [2, 1, 2, 3, 2, 4, 2, 5]
    c_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a_count = 0
    b_count = 0
    c_count = 0

    for i in range(len(answers)):
        if a_student[i % 5] == answers[i]:
            a_count += 1
        if b_student[i % 8] == answers[i]:
            b_count += 1
        if c_student[i % 10] == answers[i]:
            c_count += 1
    if a_count >= b_count and a_count >= c_count:
        answer.append(1)
        if (a_count == b_count):
            answer.append(2)
        if (a_count == c_count):
            answer.append(3)
    elif b_count >= c_count:
        answer.append(2)
        if b_count == c_count:
            answer.append(3)
    else:
        answer.append(3)
    return answer