import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

# 인접 리스트로 그래프 구성
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False] * (v + 1)
heap = [(0, 1)] # (비용, 노드) - 1번 노드부터 시작
result = 0

while heap:
    cost, node = heapq.heappop(heap)

    if visited[node]:
        continue

    visited[node] = True    # 이미 방문한 노드면 스킵
    result += cost

    # 새로 추가된 노드와 연결된 간선들을 힙에 추가
    for next_cost, next_node in graph[node]:
        if not visited[next_node]:
            heapq.heappush(heap, (next_cost, next_node))

print(result)