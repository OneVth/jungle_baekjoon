import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s1_len = len(s1)
s2_len = len(s2)


dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(1, s2_len + 1):
    for j in range(1, s1_len + 1):
        if s1[j - 1] == s2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[s2_len][s1_len])