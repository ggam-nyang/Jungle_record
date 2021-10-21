import sys
read = sys.stdin.readline

N = int(read().strip())
student_list = []
max_grade_record = [0] * 6
temp_grade_record = [0] * 6

for _ in range(N):
    grade_a, grade_b = map(int, read().split())
    student_list.append((grade_a, grade_b))

for i in range(len(student_list)):
    a_grade = student_list[i][0]
    b_grade = student_list[i][1]

    if (a_grade != b_grade):
        temp_grade_record[a_grade] += 1
        temp_grade_record[b_grade] += 1
    else:
        temp_grade_record[a_grade] += 1
    for j in range(1, 6):
        if j == a_grade or j == b_grade:
            continue
        temp_grade_record[j] = 0

    max_grade_record[a_grade] = max(max_grade_record[a_grade], temp_grade_record[a_grade])
    max_grade_record[b_grade] = max(max_grade_record[b_grade], temp_grade_record[b_grade])

max_value = max(max_grade_record)
max_index = max_grade_record.index(max_value)

print(max_value, max_index)