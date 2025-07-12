import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    repeat, target = sys.stdin.readline().split()
    repeat = int(repeat)

    result = ''.join([c * repeat for c in target])
    print(result)