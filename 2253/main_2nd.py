import sys
from math import sqrt, floor

input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
blocked = [False] * (n + 1)
for _ in range(m):
    blocked[int(input())] = True

max_v = floor(sqrt(2 * n)) + 1

dp = [[INF] * (max_v + 1) for _ in range(n + 1)]
dp[1][0] = 0

for i in range(1, n):
    if blocked[i]:
        continue

    for v in range(max_v + 1):
        if dp[i][v] == INF:
            continue

        for next_v in [v - 1, v, v + 1]:
            if next_v < 1:
                continue
            if next_v > max_v:
                continue

            next_pos = i + next_v
            if next_pos <= n and not blocked[next_pos]:
                dp[next_pos][next_v] = min(dp[next_pos][next_v], dp[i][v] + 1)

result = min(dp[n])
print(-1 if result == INF else result)