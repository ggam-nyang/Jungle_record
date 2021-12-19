import sys
import collections

read = sys.stdin.readline

emoticon_S = int(read())
## -1, 복사, 붙여넣기 중 1개의 일을 수행하면 됨
## bfs를 이용하여, 3가지를 모두 실행하며 최단 시간을 찾아봄!!

screen_emoticon = 1
storage_emoticon = 0
time = 0

queue = collections.deque()
queue.append((time, screen_emoticon, storage_emoticon))

visited = [[0] * (emoticon_S * 2) for _ in range(emoticon_S + 1)]
visited[1][0] = 1

while queue:
    # print(queue)
    now_time, now_screen, now_storage = queue.popleft()
    # print((now_time, now_screen, now_storage))
    if now_screen == emoticon_S:
        print(now_time)
        break

    if now_screen > 2:
        if visited[now_screen - 1][now_storage] == 0:
            queue.append((now_time + 1, now_screen - 1, now_storage))
            visited[now_screen - 1][now_storage] == now_time + 1
    if visited[now_screen][now_screen] == 0:
        queue.append((now_time + 1, now_screen, now_screen))
        visited[now_screen][now_screen] == now_time + 1
    if now_screen + now_storage <= emoticon_S and visited[now_screen + now_storage][now_storage] == 0:
        queue.append((now_time + 1, now_screen + now_storage, now_storage))
        visited[now_screen + now_storage][now_storage] = now_time + 1



