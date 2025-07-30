import sys
from collections import deque

input = sys.stdin.readline

def backtrack(city):
    global critical_edges

    if visited[city]:
        return
    
    visited[city] = True

    for prev_city, time in reverse_adj[city]:
        if distance[prev_city] + time == distance[city]:
            critical_edges += 1
            backtrack(prev_city)

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
reverse_adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    reverse_adj[b].append((a, c))
    indegree[b] += 1

start, end = map(int, input().split())

q = deque()
distance = [0] * (n + 1)

q.append(start)

while q:
    current = q.popleft()

    for next_city, time in adj[current]:
        distance[next_city] = max(distance[next_city], distance[current] + time)
        indegree[next_city] -= 1

        if indegree[next_city] == 0:
            q.append(next_city)

visited = [False] * (n + 1)
critical_edges = 0

backtrack(end)

print(distance[end])
print(critical_edges)

