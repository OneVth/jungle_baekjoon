import sys

input = sys.stdin.readline

INF = float('inf')

def tsp(curr, mask):
    if mask == (1 << n) - 1:
        return w[curr][0] if w[curr][0] else INF
    
    if dp[curr][mask] != -1:
        return dp[curr][mask]
    
    dp[curr][mask] = INF

    for next in range(n):
        if mask & (1 << next) == 0 and w[curr][next]:
            dp[curr][mask] = min(dp[curr][mask], tsp(next, mask | (1 << next)) + w[curr][next])

    return dp[curr][mask]

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * 2 ** n

tsp(0, 1)
print(dp)
print(w)