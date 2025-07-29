import sys
import heapq

input = sys.stdin.readline

n = int(input())
adj = []
for _ in range(n):
    adj.append([int(c) for c in input().strip()])

visited = [[False for _ in range(n)] for _ in range(n)]

pq = []
heapq.heappush(pq, (0, 0, 0)) # (비용, x, y)
visited[0][0] = True

direction = [-1, 1]

while pq:
    c, x, y = heapq.heappop(pq)

    if x == n - 1 and y == n - 1:
        print(c)
        break
    
    for dx in direction:
        new_x = x + dx
        if 0 <= new_x < n:
            if not visited[new_x][y]:
                next_cost = c + (1 - adj[new_x][y])
                heapq.heappush(pq, (next_cost, new_x, y))
                visited[new_x][y] = True
        
    for dy in direction:
        new_y = y + dy
        if 0 <= new_y < n:
            if not visited[x][new_y]:
                next_cost = c + (1 - adj[x][new_y])
                heapq.heappush(pq, (next_cost, x, new_y))
                visited[x][new_y] = True
