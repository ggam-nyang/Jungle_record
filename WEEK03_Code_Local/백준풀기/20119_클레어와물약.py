import sys
import collections

potion_N, recipe_N = map(int, sys.stdin.readline().strip().split())

potion_recipe = [[] for _ in range(potion_N + 1)]
indegree = [-1] * (potion_N + 1)  ## 가진 물약은 0, 제조에 필요한 물약의 수에 따라 indegree ++, 못만드는건?
queue = collections.deque()

for _ in range(recipe_N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    need_potion_N = temp[0]
    target_portion = temp[-1]
    for potion in temp[1: need_potion_N + 1]:
        potion_recipe[potion].append(target_portion)
    indegree[target_portion] = temp[0]

available_potion_N = int(sys.stdin.readline().strip())
available_potion = list(map(int, sys.stdin.readline().strip().split()))

for potion in available_potion:
    indegree[potion] = 0
    queue.append(potion)

while queue:
    start_potion = queue.popleft()

    for potion in potion_recipe[start_potion]:
        indegree[potion] -= 1
        if indegree[potion] == 0:
            available_potion.append(potion)
            queue.append(potion)


print(len(available_potion))
print(*sorted(available_potion))

