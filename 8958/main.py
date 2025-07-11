import sys

n = int(sys.stdin.readline())

for _ in range(n):
    result = sys.stdin.readline()
    point = 0
    total = 0
    for c in result:
        if c == 'O':
            point += 1
            total += point
        else:
            point = 0

    print(total)