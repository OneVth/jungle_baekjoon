import sys
import bisect

input = sys.stdin.readline

n = int(input())
series = list(map(int, input().split()))

lis = []
for i in range(n):
    if not lis or lis[-1] < series[i]:
        lis.append(series[i])
    else:
        idx = bisect.bisect_left(lis, series[i])
        lis[idx] = series[i]

print(len(lis))