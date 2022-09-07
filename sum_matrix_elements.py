row, colon = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0
for _ in range(row):
    rows = [int(x) for x in input().split(", ")]
    matrix.append(rows)
    matrix_sum += sum(rows)
print(matrix_sum)
print(matrix)

3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0