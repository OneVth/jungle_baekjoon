import sys

input = sys.stdin.readline

n = int(input())

mat_info = []
for _ in range(n):
    r, c = map(int, input().split())
    mat_info.append((r, c))

INF = float('inf')
dp = [[0 if i == j else INF for j in range(n)] for i in range(n)]

for length in range(2, n + 1):  # 구간 길이
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + mat_info[i][0] * mat_info[k][1] * mat_info[j][1]
            dp[i][j] = min(dp[i][j], cost)


print(dp[0][n - 1])