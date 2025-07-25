import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

adjacent = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    adjacent[a].append((cost, b))
    adjacent[b].append((cost, a))

visited = [False] * (v + 1)
heap = [(0, 1)]  # (비용, 노드) 1번 노드부터 시작
result = 0

while heap:
    cost, node = heapq.heappop(heap)

    # 이미 방문한 노드면 스킵
    if visited[node]:
        continue

    visited[node] = True
    result += cost

    for next_cost, next_node in adjacent[node]:
        if not visited[next_node]:
            heapq.heappush(heap, (next_cost, next_node))


print(result)
