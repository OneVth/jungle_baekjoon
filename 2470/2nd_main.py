import sys
import bisect

input = sys.stdin.readline

n = int(input())
values = sorted(map(int, input().split()))

min_sum = int(10e9)
ans = [0] * 2 # 출력할 용액의 특성값

for i in range(n - 1):
    a = values[i]
    target = -a

    # target과 가장 가까운 값을 이분 탐색
    idx = bisect.bisect_left(values, target, i + 1, n)

    # idx - 1 혹은 idx가 i와 같거나, len(values)와 같은 경우를 배제
    for j in [idx - 1, idx]:
        if j <= i or j >= n:
            continue

        b = values[j]
        total = abs(a + b)
        if total < min_sum:
            min_sum = total
            ans = [a, b]

print(*ans)
