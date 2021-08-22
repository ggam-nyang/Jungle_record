import sys
import collections

R, C = map(int, sys.stdin.readline().strip().split())

alphabet_list = []
for _ in range(R):
    alphabet_list.append(list(sys.stdin.readline().strip()))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


## DFS
# now_record = []
# now_record.append(alphabet_list[0][0])

# ans = 1
# def dfs(x, y, count):
#     global ans

#     ans = max(ans, count)

#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]

#         if 0 <= new_x < R and 0 <= new_y < C and alphabet_list[new_x][new_y] not in now_record:
#                 now_record.append(alphabet_list[new_x][new_y])
#                 dfs(new_x, new_y, count + 1)
#                 now_record.remove(alphabet_list[new_x][new_y])

# dfs(0, 0, ans)
# print(ans)


# queue = collections.deque()
# queue.append((0, 0))


# while queue:
#     x, y = queue.popleft()
#     checker[x][y] = 1

#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]

#         if 0 <= new_x < R and 0 <= new_y < C and checker[new_x][new_y] == 0:
#             for alpha in alphabet_list[new_x][new_y]:
#                 if alpha in alphabet_list[x][y]:
#                     is_poss = False
#                     break
#                 is_poss = True
#             if is_poss:
#                 queue.append((new_x, new_y))
#                 alphabet_list[new_x][new_y] = alphabet_list[x][y] + alphabet_list[new_x][new_y]
# print(alphabet_list)



answer = 1
def bfs(row, col):
    global answer
    queue = set([(row, col, alphabet_list[row][col])])

    while queue:
        x, y, temp = queue.pop()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < R and 0 <= new_y < C and alphabet_list[new_x][new_y] not in temp:
                queue.add((new_x, new_y, temp + alphabet_list[new_x][new_y]))
                answer = max(answer, len(temp) + 1)

bfs(0, 0)
print(answer)