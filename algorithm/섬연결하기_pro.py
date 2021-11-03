import itertools

# def solution(n, costs):
#     answer = 0
#     link_num = len(costs)
#     linked_count = [0] * n
#     for link in costs:
#         linked_count[link[0]] += 1
#         linked_count[link[1]] += 1

#     costs.sort(key=lambda x : x[2], reverse=True)

#     # index_arr = []
#     # for i in range(len(costs)):
#     #     index_arr.append(i)

#     for temp_links in itertools.combinations(range(link_num), link_num - n + 1):
#         check = True

#         for island in temp_links:
#             linked_count[costs[island][0]] -= 1
#             linked_count[costs[island][1]] -= 1
#             if linked_count[costs[island][0]] <= 0 or linked_count[costs[island][1]] <= 0:
#                 check = False

#         if not check:
#             for island in temp_links:
#                 linked_count[costs[island][0]] += 1
#                 linked_count[costs[island][1]] += 1

#         if check:
#             high_costs = temp_links
#             break


#     for i in costs:
#         answer += i[2]

#     for j in high_costs:
#         answer -= costs[j][2]

#     return answer



def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    print(costs)
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
        print(connect)
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer