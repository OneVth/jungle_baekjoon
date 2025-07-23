import sys

sys.setrecursionlimit(10**8)

def cal_color_paper(table, n):
    if n <= 0:
        return 0, 0    

    for i in range(n):
        if not all(table[i]):
            break
    else:
        return 0, 1
    
    for i in range(n):
        if any(table[i]):
            break
    else:
        return 1, 0


    n //= 2
    table1 = [table[i][:n] for i in range(n)]
    table2 = [table[i][n:] for i in range(n)]
    table3 = [table[n + i][:n] for i in range(n)]
    table4 = [table[n + i][n:] for i in range(n)]

    w1, b1 = cal_color_paper(table1, n)
    w2, b2 = cal_color_paper(table2, n)
    w3, b3 = cal_color_paper(table3, n)
    w4, b4 = cal_color_paper(table4, n)

    return w1 + w2 + w3 + w4, b1 + b2 + b3 + b4

input = sys.stdin.readline

n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]

w, b = cal_color_paper(table, n)
print(w, b)