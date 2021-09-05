import sys
read = sys.stdin.readline

# 테스트 케이스
T = int(read().strip())

for _ in range(T):
    log_N = int(read().strip())
    log_list = list(map(int, read().strip().split()))

    # 오름차순으로 정렬한다.
    log_list.sort()
    level = 0
    # 남은 통나무 중, 최솟값을 왼쪽 오른쪽 끝에 차곡차곡 배열한다. 이때가 가장 통나무 간의 높이 차가 작을 때이다
    # 이를 계산하기 위해 오름차순 정렬 후, 1 3 5 7... 을 비교하고 2 4 6 8...을 비교한다
    for i in range(2, len(log_list), 2):
        temp = log_list[i] - log_list[i - 2]
        level = max(level, temp)

    for j in range(3, len(log_list), 2):
        temp = log_list[j] - log_list[j - 2]
        level = max(level, temp)

    # 통나무는 원형으로 배치되므로, 체크하지 못하는 경우가 2가지가 생긴다. 맨처음 통나무와 마지막 통나무 그리고 가운데 나란히 있는 가장 긴 통나무들
    level = max(level, log_list[1] - log_list[0], log_list[-1] - log_list[-2])

    print(level)