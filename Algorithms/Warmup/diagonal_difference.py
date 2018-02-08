def SumDiagonal(matrix, n):
    diagonal1_sum = 0

    for line in range(n):
        for column in range(n):
            if line == column:
                diagonal1_sum += matrix[line][column]

    return diagonal1_sum

def SumReverseDiagonal(matrix, n):
    diagonal2_sum = 0
    column = n
    for line in range(n):
        diagonal2_sum += matrix[line][column-1]
        column = column - 1

    return diagonal2_sum


n = int(input())
matrix = [list(map(int, input().strip().split(' '))) for i in range(n)]

result_sum_diagonal1 = SumDiagonal(matrix, n)
result_sum_diagonal2 = SumReverseDiagonal(matrix,n)
print(abs(result_sum_diagonal1 - result_sum_diagonal2))
