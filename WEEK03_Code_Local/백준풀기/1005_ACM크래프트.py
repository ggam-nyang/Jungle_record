import collections
import sys

T = int(sys.stdin.readline().strip())


for _ in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())
    building_time = [0] + list(map(int, sys.stdin.readline().strip().split()))

    building_list = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    queue = collections.deque()

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().strip().split())
        building_list[a].append(b)
        indegree[b] += 1
    winning_building = int(sys.stdin.readline().strip())


    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)


    time_list = building_time[::]
    total_time = 0

    ## 약간 dp의 개념을 섞은 느낌
    while queue:
        start_node = queue.popleft()
        if start_node == winning_building:
            break
        for node in building_list[start_node]:
            time_list[node] = max(time_list[node], time_list[start_node] + building_time[node])
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)

    print(time_list[start_node])




    # while queue:
    #     max_time = 0
    #     for _ in range(len(queue)):
    #         start_node = queue.popleft()
    #         max_time = max(max_time, building_time[start_node - 1])
    #         for node in building_list[start_node]:
    #             indegree[node] -= 1
    #             if indegree[node] == 0:
    #                 queue.append(node)
    #         time_list[start_node] = total_time + building_time[start_node - 1]
    #     total_time += max_time