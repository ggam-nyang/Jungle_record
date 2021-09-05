import sys
read = sys.stdin.readline


T = int(read().strip())
for _ in range(T):
    applicant_N = int(read().strip())
    applicant_list = []
    for _ in range(applicant_N):
        applicant_list.append(list(map(int, read().strip().split())))




    applicant_list.sort()
    fix = applicant_list[0][1]
    count = 1
    for i in range(1, applicant_N):
        if fix > applicant_list[i][1]:
            count += 1
            fix = applicant_list[i][1]

    print(count)