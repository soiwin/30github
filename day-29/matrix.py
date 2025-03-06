

n = 8
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 2


for i in range(n):
    print(*matrix[i])
