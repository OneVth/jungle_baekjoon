import sys

sys.setrecursionlimit(10**8)

n, b = map(int, input().split())

def multiply(mat1, mat2):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000

    return result

def pow_matrix(mat, exp):
    if exp == 1:
        return [[element % 1000 for element in row] for row in mat]
    
    half = pow_matrix(mat, exp // 2)

    result = multiply(half, half)
    if exp % 2 == 1:
        result = multiply(result, mat)

    return result


input = sys.stdin.readline

mat = [list(map(int, input().split())) for _ in range(n)]

result = pow_matrix(mat, b)
for row in result:
    print(*row)