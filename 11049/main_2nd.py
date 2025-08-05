import sys

input = sys.stdin.readline
INF = float('inf')

n = int(input())
dimensions = []
for _ in range(n):
    p, q = map(int, input().split())
    dimensions.append((p, q))

dp = [[0] * n for _ in range(n)]
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = INF 
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + dimensions[i][0] * dimensions[k][1] * dimensions[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n - 1])