def solution(gems):
    answer = []

    numbering = 0
    gems_dict = {}
    for gem in gems:
        try: gems_dict[gem]

        except:
            gems_dict[gem] = numbering
            numbering += 1
    total_gem = len(gems_dict)
    check_gem = [0] * total_gem

    total_count = 0
    ans_min = 0
    ans_max = 100001
    for i in range(len(gems)):
        gem_number = gems_dict[gems[i]]

        if check_gem[gem_number] == 0:
            check_gem[gem_number] = i + 1
            total_count += 1

        else:
            check_gem[gem_number] = i + 1

        if total_count == total_gem:
            temp_min = min(check_gem)
            temp_max = i + 1
            if (temp_max - temp_min < ans_max - ans_min):
                ans_min = temp_min
                ans_max = temp_max

                if (ans_max - ans_min == total_gem - 1):
                    return [ans_min, ans_max]
    answer = [ans_min, ans_max]
    return answer


