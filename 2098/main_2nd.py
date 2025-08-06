import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def tsp(curr, mask):
    # 모든 도시를 방문했다면 시작점으로 돌아가는 비용
    if mask == (1 << n) - 1:
        return mat[curr][0] if mat[curr][0] else float('inf')
    
    # 이미 계산된 값이 있으면 반환
    if dp[curr][mask] != -1:
        return dp[curr][mask]
    
    # 최솟값 초기화
    dp[curr][mask] = float('inf')

    # 아직 방문하지 않은 모든 도시를 확인
    for next in range(n):
        # next 도시를 방문하지 않았고, 갈 수 있는 경로가 있다면
        if mask & (1 << next) == 0 and mat[curr][next]:
            # 재귀 호출하여 최솟값 갱신
            dp[curr][mask] = min(dp[curr][mask], tsp(next, mask | (1 << next)) + mat[curr][next])
    return dp[curr][mask]

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (1 << n) for _ in range(n + 1)]

tsp(0, 1)

print(dp[0][1])
