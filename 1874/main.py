import sys

input = sys.stdin.readline

n = int(input())

seq = []
for _ in range(n):
    seq.append(int(input()))

stack = []
result = []
cur = 0
for i in range(1, n + 1):
    stack.append(i)
    result.append('+')

    while stack and stack[-1] == seq[cur]:
        stack.pop()
        result.append('-')
        cur += 1

if stack:
    print('NO')
else:
    for c in result:
        print(c)