import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(vertex):
    visited[vertex] = True
    indoor_count = 0

    for v in adj[vertex]:
        if is_inside[v]:
            indoor_count += 1
        elif not visited[v]:
            indoor_count += dfs(v)
    return indoor_count


n = int(input())
line = input().strip()
is_inside = [0]
for i in range(len(line)):
    is_inside.append(int(line[i]))

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)
result = 0

for i in range(1, n + 1):
    if is_inside[i]:
        for v in adj[i]:
            if is_inside[v] and i < v:
                result += 2

for i in range(1, n + 1):
    if not is_inside[i] and not visited[i]:
        indoor_count = dfs(i)
        result += indoor_count * (indoor_count - 1)

print(result)
