import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

adjacent = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

result = 1
q = deque()
q.append(1) # 1번 정점부터 탐색 시작
for i in range(2, n + 1):
    while q:
        vertex = q.popleft()

        if visited[vertex]:
            continue

        visited[vertex] = True
        for v in adjacent[vertex]:
            if not visited[v]:
                q.append(v)

    if not visited[i]:
        q.append(i)
        result += 1

print(result)
