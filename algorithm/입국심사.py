def solution(n, times):
    answer = 0


    start = 1
    end = n * times[0]
    times.sort()
    temp_answer = []


    while start <= end:
        mid = (start + end) // 2


        temp_count = 0
        for i in range(len(times)):
            temp_count += mid // times[i]

        if temp_count >= n:
            end = mid - 1
            temp_answer.append(mid)
        else:
            start = mid + 1

    # if not temp_answer:
    #     return times[0] * n

    answer = min(temp_answer)
    return answer