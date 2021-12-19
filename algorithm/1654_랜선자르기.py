import sys
read = sys.stdin.readline

K, N = map(int, read().strip().split())
wire_list = []
for _ in range(K):
    wire_list.append(int(read()))

start = 1
end = max(wire_list)
answer = []

while start <= end:
    mid = (start + end) // 2
    wire_count = 0

    for wire in wire_list:
        wire_count += wire // mid

    if wire_count < N:
        end = mid - 1

    else:
        start = mid + 1

print(end)
# print(max(answer))