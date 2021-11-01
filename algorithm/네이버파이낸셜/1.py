def solution(id_list, k):
    answer = 0
    coupon_count_dict = {}

    for today_ids in id_list:
        temp_check_list = []
        today_id_list = today_ids.split(" ")
        for id in today_id_list:
            try:
                if coupon_count_dict[id] < k and id not in temp_check_list:
                    coupon_count_dict[id] += 1
            except:
                coupon_count_dict[id] = 1
            temp_check_list.append(id)
    for coupon in coupon_count_dict.values():
        answer += coupon

    return answer