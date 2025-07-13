import sys

n = int(sys.stdin.readline().strip())

table = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline().strip())
    table[num - 1] += 1

for i in range(10001):
    for _ in range(table[i]):
        print(i + 1)