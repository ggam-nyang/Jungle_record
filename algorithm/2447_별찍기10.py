import sys
star_N = int(sys.stdin.readline())

# star_record = [0] * (3 ** 7 + 1)
# star_record[3] = ['***', '* *', '***']
# def make_star(n):
#     star_list = [''] * int(n)
#     if (n == 3):
#         return star_record[3]

#     small_case = n // 3
#     if star_record[small_case] != 0:
#         little_star_list = star_record[small_case]
#     else:
#         little_star_list = make_star(small_case)
#     for i in range(n):
#         if small_case <= i < small_case * 2:
#             star_list[i] = little_star_list[i % small_case] + ' ' * small_case + little_star_list[i % small_case]
#         else:
#             star_list[i] = small_case * little_star_list[i % small_case]
#     return star_list

def make_star(n):
    if n == 1:
        return ['*']

    stars = make_star(n // 3)
    star_list = []
    for s in stars:
        star_list.append(s * 3)
    for s in stars:
        star_list.append(s + ' ' * (n // 3) + s)
    for s in stars:
        star_list.append(s * 3)
    return star_list

print('\n'.join(make_star(star_N)))
