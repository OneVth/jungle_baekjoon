import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque(range(1, n + 1))
result = []
while queue:
    for _ in range(k):
        val = queue.popleft()
        queue.append(val)
    result.append(queue.pop())

print('<', end='')
for i in range(len(result) - 1):
    print(f'{result[i]}, ', end='')
print(result[-1], end='')
print('>')