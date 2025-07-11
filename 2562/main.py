import sys

max = int(-1e9)

try:
    i = 0
    idx = 0
    while True:
        n = int(sys.stdin.readline())
        if n > max:
            max = n
            idx = i
        i += 1

except:
    print(max)
    print(idx + 1)  # idx + 1 번째
    exit()
