import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
len_s1 = len(s1)
len_s2 = len(s2)

dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len_s1][len_s2])