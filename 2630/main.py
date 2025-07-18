import sys

sys.setrecursionlimit(10**8)

def divide(n, table):
    """
    n * n 배열인 table이 모두 0 or 1인지 확인하는 함수입니다.
    """
    if n <= 0:
        return 0, 0

    """table의 모든 요소가 1인지 확인"""
    for i in range(n):
        if not all(table[i]):
            break
    else:
        return 0, 1

    """table의 모든 요소가 0인지 확인"""
    for i in range(n):
        if any(table[i]):
            break
    else:
        return 1, 0

    n //= 2
    table1 = [table[i][0:n] for i in range(n)]
    table2 = [table[i][n : 2 * n] for i in range(n)]
    table3 = [table[i][0:n] for i in range(n, 2 * n)]
    table4 = [table[i][n : 2 * n] for i in range(n, 2 * n)]

    w1, b1 = divide(n, table1)
    w2, b2 = divide(n, table2)
    w3, b3 = divide(n, table3)
    w4, b4 = divide(n, table4)

    return w1 + w2 + w3 + w4, b1 + b2 + b3 + b4


n = int(sys.stdin.readline())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

w, b = divide(n, table)
print(w, b)
