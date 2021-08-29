import sys

meeting_N = int(sys.stdin.readline().strip())

# meeting_data: 전체 입력 값, possible_meetings: 정답을 담을 list
meeting_data = []
possible_meetings = []
for _ in range(meeting_N):
    start, end = map(int, sys.stdin.readline().strip().split())
    meeting_data.append((start, end))

# 회의가 끝나는 시간으로 정렬 (같을 경우 시작 시간으로 정렬)
meeting_data.sort(key=lambda x : (x[1], x[0]))

if meeting_data[0][1] >= meeting_data[0][0]:
    possible_meetings.append(meeting_data[0])

# 일찎 끝나는 회의를 무조건 먼저 한다! 마지막 회의의 종료시간보다는 시작 시간이 늦어야한다.
for meeting in meeting_data[1:]:
    if possible_meetings[-1][1] <= meeting[0]:
        possible_meetings.append(meeting)

print(len(possible_meetings))