import sys

# 컴퓨터의 개수 (Node의 개수)
computer_N = int(sys.stdin.readline().strip())
# 연결의 개수 (간선의 개수)
computer_connect = int(sys.stdin.readline().strip())

# 컴퓨터 연결 상태를 2차원 배열로 저장
network = [[] for _ in range(computer_N + 1)]

for i in range(computer_connect):
    com1, com2 = map(int, sys.stdin.readline().strip().split())
    network[com1].append(com2)
    network[com2].append(com1)

# virus가 있는지 dfs로 탐색하는 함수
def check_virus(net, start, visited = []):
    visited.append(start)

    for connect_computer in net[start]:
        if connect_computer not in visited:
            check_virus(net, connect_computer, visited)

    return visited

print(len(check_virus(network, 1, [])) - 1)