import sys
from collections import deque

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def dfs(vertex):
    if visited[vertex]:
        return
    
    visited[vertex] = True
    print(vertex, end=' ')

    for v in adjacent[vertex]:
        if not visited[v]:
            dfs(v)

def bfs(q: deque):
    while q:
        vertex = q.popleft()

        if visited[vertex]:
            continue

        visited[vertex] = True
        print(vertex, end=' ')
        for v in adjacent[vertex]:
            if not visited[v]:
                q.append(v)


n, m, v = map(int, input().split())

adjacent = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

# 정점 번호가 작은 것을 먼저 방문할 수 있도록 정렬
for i in range(1, n + 1):
    adjacent[i].sort()

visited = [False] * (n + 1)
dfs(v)  # v번 정점부터 탐색 시작
print()

visited = [False] * (n + 1)
q = deque()
q.append(v) # 1번 정점부터 탐색 시작
bfs(q)