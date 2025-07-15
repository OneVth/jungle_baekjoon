import sys

MAX_INPUT = 10001

# 에라토스테네스의 체 초기화
table = [True] * MAX_INPUT
table[0] = table[1] = False

for i in range(2, MAX_INPUT):
    if i * i > MAX_INPUT:
        break

    if table[i] == True:
        for j in range(i + i, MAX_INPUT, i):
            table[j] = False

n = int(sys.stdin.readline())

for _ in range(n):
    even = int(sys.stdin.readline())
    half = even // 2
    for i in range(half, -1, -1):
        if table[i] and table[even - i]:
            print(i, even - i)
            break
