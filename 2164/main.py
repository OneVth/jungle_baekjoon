import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()
    val = queue.popleft()
    queue.append(val)

print(queue.pop())