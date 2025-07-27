# BOJ 2252번 - 줄 세우기 (위상 정렬 - DFS 방식)
import sys
from collections import deque

# 깊은 재귀를 위한 재귀 한도 설정
sys.setrecursionlimit(10**8)

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# DFS를 이용한 위상 정렬 함수
def dfs(u):
    # 이미 방문한 노드면 종료
    if visited[u]:
        return
    
    # 현재 노드 방문 처리
    visited[u] = True
    
    # 인접한 모든 노드에 대해 DFS 수행
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

    # 후위 순회 방식으로 결과에 추가 (가장 나중에 추가되는 순서)
    result.appendleft(u)

# n: 학생 수, m: 키 비교 횟수
n, m = map(int, input().split())
# 인접 리스트로 그래프 표현 (방향 그래프)
adj = [[] for _ in range(n + 1)]
# 방문 여부 체크 배열
visited = [False] * (n + 1)

# 키 비교 정보 입력 (u가 v보다 앞에 서야 함)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)  # u -> v 방향 간선

# 위상 정렬 결과를 저장할 deque
result = deque()

# 모든 노드에 대해 DFS 수행 (연결되지 않은 컴포넌트 처리)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

# 위상 정렬 결과 출력
print(*result)