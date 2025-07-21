import sys
import heapq

n = int(sys.stdin.readline())

pq = []
for _ in range(n):
    heapq.heappush(pq, int(sys.stdin.readline()))

result = 0
while len(pq) > 1:
    s = heapq.heappop(pq) + heapq.heappop(pq)
    heapq.heappush(pq, s)
    result += s

print(result)

