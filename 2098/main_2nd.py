import sys

input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')] * (1 << n) for _ in range(n)]
dp[0][1] = 0

for mask in range(1, 1 << n):
    for curr in range(n):
        if mask & (1 << curr):
            for next in range(n):
                if mask & (1 << next) == 0 and mat[curr][next]:
                    new_mask = mask | (1 << next)
                    dp[next][new_mask] = min(dp[next][new_mask], dp[curr][mask] + mat[curr][next])

result = float('inf')
full_mask = (1 << n) - 1
for i in range(1, n):
    if mat[i][0]:
        result = min(result, dp[i][full_mask] + mat[i][0])

print(result)

