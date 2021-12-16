import sys
read = sys.stdin.readline

N = int(read())

paper_graph = []
for _ in range(N):
    temp_row = list(map(int, read().strip().split()))
    paper_graph.append(temp_row)

answer = [0, 0, 0]

def count_paper(col, row, length):
    if length == 1:
        answer[paper_graph[row][col] + 1] += 1
        return

    for r in range(row, row + length):
        for c in range(col, col + length):
            if paper_graph[row][col] != paper_graph[r][c]:
                new_length = length // 3
                for row_i in range(0, length, new_length):
                    for col_i in range(0, length, new_length):
                        count_paper(col + col_i, row + row_i, new_length)
                return


    answer[paper_graph[row][col] + 1] += 1

count_paper(0, 0, N)
print(*answer, sep='\n')

# print(*paper_graph, sep='\n')