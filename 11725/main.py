# BOJ 11725 - 트리의 부모 찾기
# DFS(깊이 우선 탐색)를 사용하여 각 노드의 부모를 찾는 문제
# 시간복잡도: O(N), 공간복잡도: O(N)

import sys

# 깊은 재귀를 위한 재귀 한도 설정 (최대 100,000개 노드)
sys.setrecursionlimit(10**8)

# 빠른 입력을 위한 readline 사용
input = sys.stdin.readline

# DFS 함수 - 트리를 탐색하며 각 노드의 부모 설정
def dfs(root):
    # 이미 방문한 노드면 종료 (중복 방문 방지)
    if visited[root]:
        return
    
    # 현재 노드를 방문 처리
    visited[root] = True
    
    # 인접한 모든 노드 확인
    for v in adj[root]:
        # 방문하지 않은 노드만 처리 (부모 -> 자식 방향으로만 이동)
        if not visited[v]:
            # 현재 노드를 자식 노드의 부모로 설정
            parent[v] = root
            # 자식 노드에 대해 재귀적으로 DFS 수행
            dfs(v)

# 입력 처리: 노드의 개수
n = int(input())

# 인접 리스트로 트리 구조 표현 (1번부터 n번까지 사용)
adj = [[] for _ in range(n + 1)]

# 트리의 간선 정보 입력 (n-1개의 간선)
for _ in range(n - 1):
    u, v = map(int, input().split())
    # 무방향 그래프이므로 양방향으로 연결
    adj[u].append(v)
    adj[v].append(u)

# 각 노드의 부모를 저장할 배열 (0으로 초기화)
parent = [0] * (n + 1)
# 노드 방문 여부를 체크할 배열
visited = [False] * (n + 1)

# 루트 노드(1번)부터 DFS 시작
dfs(1)

# 결과 출력: 2번 노드부터 n번 노드까지의 부모 출력
for i in parent[2:]:
    print(i)