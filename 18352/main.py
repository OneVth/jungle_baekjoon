# BOJ 18352번 - 특정 거리의 도시 찾기 (BFS)
import sys
from collections import deque

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# n: 도시 개수, m: 도로 개수, k: 거리 정보, x: 출발 도시
n, m, k, x = map(int, input().split())
# 인접 리스트로 그래프 표현 (1번부터 n번까지)
adj = [[] for _ in range(n + 1)]
# 방문 여부 체크 배열
visited = [False] * (n + 1)

# 단방향 도로 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

# BFS를 위한 큐 초기화
q = deque()
# 출발 도시를 거리 0으로 큐에 추가
q.append((x, 0))
# 출발 도시 방문 처리
visited[x] = True

# 거리 k인 도시들을 저장할 리스트
result = []

# BFS 실행
while q:
    u, d = q.popleft()
    
    # 거리가 k인 도시를 찾으면 결과에 추가
    if d == k:
        result.append(u)
        continue  # 더 이상 탐색하지 않음

    # 현재 도시에서 연결된 모든 도시 탐색
    for v in adj[u]:
        if not visited[v]:
            # 거리를 1 증가시켜 큐에 추가
            q.append((v, d + 1))
            visited[v] = True

# 결과 출력 (오름차순 정렬)
result.sort()
if result:
    for v in result:
        print(v)
else:
    print(-1)  # 거리 k인 도시가 없는 경우