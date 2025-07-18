import sys
import bisect

n = int(sys.stdin.readline())

values = sorted(list(map(int, sys.stdin.readline().split())))


min_sum = int(10e9)
ans = [0] * 2   # 출력할 용액의 특성값
for i in range(n - 1):
    a = values[i]
    target = -a

    idx = bisect.bisect_left(values, target, i + 1, n)

    for j in [idx - 1, idx]:
        if j <= i or j >= n:
            continue
        
        b = values[j]
        total = abs(a + b)
        if total < min_sum:
            min_sum = total
            ans = [a, b]


print(ans[0], ans[1])
