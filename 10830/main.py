import sys

n, b = map(int, sys.stdin.readline().split())


def multiply(left, right):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += left[i][k] * right[k][j]
            result[i][j] %= 1000
    return result


def pow_matrix(mat, exp):
    if exp == 1:
        return mat

    half = pow_matrix(mat, exp // 2)
    if exp % 2 == 0:
        return multiply(half, half)
    else:
        return multiply(multiply(half, half), mat)


a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for r in pow_matrix(a, b):
    print(*r)
