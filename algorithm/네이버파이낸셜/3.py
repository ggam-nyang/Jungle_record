def solution(logs):
    answer = []
    global log_dict
    log_dict = {}
    # log를 분석하여 각 수험번호 별 푼 문제를 각각의 dict에 담는다.

    for log in logs:
        test_id, prob_num, score = log.split(' ')
        if log_dict.get(test_id):
            log_dict[test_id][prob_num] = score
        else:
            log_dict[test_id] = {}
            log_dict[test_id][prob_num] = score

    tester_list = list(log_dict.keys())
    # print(comp_answer(tester_list[0], tester_list[1]))
    for i in range(len(log_dict)):
        for j in range(i + 1, len(log_dict)):
            # print(i, log_dict[tester_list[i]])
            if log_dict[tester_list[j]] in answer:
                continue

            if comp_answer(tester_list[i], tester_list[j]):
                if tester_list[i] not in answer:
                    answer.append(tester_list[i])

                if tester_list[j] not in answer:
                    answer.append(tester_list[j])

    answer.sort()

    if answer == []:
        answer.append("None")

    return answer


def comp_answer(a_tester, b_tester):

    if len(log_dict[a_tester]) != len(log_dict[b_tester]):
        return False

    if len(log_dict[a_tester]) < 5:
        return False

    for prob in log_dict[a_tester].keys():
        if (not log_dict[b_tester].get(prob)):
            return False

        if (log_dict[a_tester][prob]) != log_dict[b_tester][prob]:
            return False

    return True

