import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

adjacent = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for _ in range(e):
    a, b, cost = map(int, input().split())
    adjacent[a].append((cost, b))
    adjacent[b].append((cost, a))

heap = [(0, 1)] # (비용, 정점)
result = 0

while heap:
    cost, vertex = heapq.heappop(heap)
    if visited[vertex]:
        continue

    visited[vertex] = True
    result += cost
    for cost, a in adjacent[vertex]:
        if not visited[a]:
            heapq.heappush(heap, (cost, a))

print(result)
