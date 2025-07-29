import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start, end, n):
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == end:
            return distances[end]
        
        for c, v in adj[current_vertex]:
            distance = current_distance + c

            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))

    return distances[end]

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    adj[u].append((c, v))   # (비용, 도착지)

st, dst = map(int, input().split())

result = dijkstra(adj, st, dst, n)
print(result)