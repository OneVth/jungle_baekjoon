import sys

input = sys.stdin.readline

INF = float('inf')

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# dp[mask][curr] = mask 상태에서 curr 도시에 있을 때 남은 경로의 최소 비용
dp = [[INF] * n for _ in range(1 << n)]

# 모든 도시를 방문한 상태에서 시작점으로 돌아가는 비용
for i in range(n):
    if w[i][0]:  # i에서 0으로 가는 경로가 있으면
        dp[(1 << n) - 1][i] = w[i][0]

# 상향식으로 DP 테이블 채우기
for mask in range((1 << n) - 2, 0, -1):  # 모든 도시 방문 상태에서 역순으로
    for curr in range(n):
        if not (mask & (1 << curr)):  # curr 도시를 방문하지 않은 상태면 skip
            continue
            
        for next in range(n):
            if mask & (1 << next) or not w[curr][next]:  # 이미 방문했거나 경로가 없으면 skip
                continue
            
            next_mask = mask | (1 << next)
            dp[mask][curr] = min(dp[mask][curr], dp[next_mask][next] + w[curr][next])

print(dp[1][0])