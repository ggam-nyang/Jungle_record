import sys
import collections
read = sys.stdin.readline

stone_N, small_stone_M = map(int, read().strip().split())

small_stone = [int(read().strip()) for _ in range(small_stone_M)]


queue = collections.deque()




def bfs(x, dist):
    visted = [0] * (stone_N + 1)
    visted[x] = 1
    queue.append((x, dist, 0, []))
    while queue:
        now_x, jump_dist, count, past_way = queue.popleft()
        # print(now_x, count)
        if now_x == stone_N:
            return count

        for dx in [-1, 0, 1]:
            new_dist = jump_dist + dx
            new_x = now_x + new_dist
            if new_x in small_stone:
                continue
            if 0 < new_dist and new_x <= stone_N and visted[new_x] == 0:
                queue.append((new_x, new_dist, count + 1))
                visted[new_x] = 1
    return -1
print(bfs(1, 0))
