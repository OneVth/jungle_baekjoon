import sys
import bisect

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

lis = []
for x in arr:
    idx = bisect.bisect_left(lis, x)
    if idx == len(lis):
        lis.append(x)
    else:
        lis[idx] = x
print(len(lis))

