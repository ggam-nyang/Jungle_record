import sys
import collections
read = sys.stdin.readline

computer_N = int(read())
edge = int(read())
network_graph = [[] for _ in range(computer_N + 1)]
queue_check = [1]

for _ in range(edge):
    start, end = map(int, read().split())
    network_graph[start].append(end)
    network_graph[end].append(start)

queue = collections.deque()

queue.append(1)
count = 0
virus_list = set()


while queue:
    virus_computer = queue.popleft()

    for com in network_graph[virus_computer]:
        if com not in queue_check:
            virus_list.add(com)
            queue.append(com)
            queue_check.append(com)

# print(count)
print(len(virus_list))