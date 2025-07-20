import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    line = sys.stdin.readline().split()

    command = line[0]
    if command == 'push':
        queue.append(line[1])

    elif command == 'pop':
        try:
            val = queue.popleft()
            print(val)
        except:
            print(-1)

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

