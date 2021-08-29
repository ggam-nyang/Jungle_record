import sys
read = sys.stdin.readline

tab_N, using_K = map(int, read().strip().split())

elec_items = list(map(int, read().strip().split()))


# 0번 인덱스에는 현재 꽃힌 item, 1번 인덱스에는 그 item이 또 등장하는 다음 index를 담았다.
# 공간복잡도가 비효율적인 것 같다. (추측)
now_items = [[], []]

# 플러그를 빼는 횟수 카운트
count = 0
for i in range(len(elec_items)):
    item = elec_items[i]
    # 안꽃힌 플러그를 꽃아야 하는 경우, now_items[1]의 가장 작은 인덱스를 빼주고, 새로운 플러그의 값, 그 플러그의 다음 값을 기록한다. count를 하나 올린다.
    if item not in now_items[0]:
        if len(now_items[0]) == tab_N:
            try:
                remove_idx = now_items[1].index(-1)
            except:
                remove_idx = now_items[1].index(max(now_items[1]))
            del now_items[0][remove_idx]
            del now_items[1][remove_idx]

            try:
                temp = elec_items.index(item, i + 1)
            except:
                temp = -1
            now_items[0].append(item)
            now_items[1].append(temp)
            count += 1
        else:
            now_items[0].append(item)
            try:
                temp_idx = elec_items.index(item, i + 1)
            except:
                temp_idx = -1
            now_items[1].append(temp_idx)
    # 이미 꽃힌 플러그의 경우, count를 올리지 않고 해당 플러그의 다음 올 index만 최신화 해준다.
    else:
        temp_idx = now_items[0].index(item)
        try:
            now_items[1][temp_idx] = elec_items.index(item, i + 1)
        except:
            now_items[1][temp_idx] = -1


print(count)