def rotate_matrix_90_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - 1 - i] = matrix[i][j]
    return new_matrix

n, m = map(int, input().strip().split())
input_matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    input_matrix.append(row)

output_matrix = rotate_matrix_90_clockwise(input_matrix)

for row in output_matrix:
    print(" ".join(map(str, row)))
