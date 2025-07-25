import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

adjacent = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

result = 0
q = deque()
q.append(1)
while q:
    vertex = q.popleft()
    if visited[vertex]:
        continue

    visited[vertex] = True
    result += 1
    for v in adjacent[vertex]:
        if not visited[v]:
            q.append(v)

print(result - 1)  # 1번 컴퓨터를 제외
