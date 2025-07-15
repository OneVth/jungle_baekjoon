import sys

n = int(sys.stdin.readline())

table = [0] * 100001
max_val = 0

for _ in range(n):
    val = int(sys.stdin.readline())
    max_val = max(val, max_val)

    table[val] += 1

for i in range(1, max_val + 1):
    for _ in range(table[i]):
        print(i)

