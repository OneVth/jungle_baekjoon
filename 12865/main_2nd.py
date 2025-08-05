import sys

input = sys.stdin.readline

n, k = map(int, input().split())

items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i, item in enumerate(items):
    weight, value = item
    for w in range(1, k + 1):
        if w >= weight:
            dp[i + 1][w] = max(dp[i][w], dp[i][w - weight] + value)
        else:
            dp[i + 1][w] = dp[i][w]

print(dp[n][k])
    
