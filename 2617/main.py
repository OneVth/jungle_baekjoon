import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(graph, start, visited):
    count = 0
    visited[start] = True

    for next_node in graph[start]:
        if not visited[next_node]:
            count += 1 + dfs(graph, next_node, visited)
    return count


n, m = map(int, input().split())

heavy = [[] for _ in range(n + 1)]
light = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    heavy[b].append(a)
    light[a].append(b)

result = 0
mid = (n + 1) // 2

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    heavy_count = dfs(heavy, i, visited)

    visited = [False] * (n + 1)
    light_count = dfs(light, i, visited)

    if heavy_count >= mid or light_count >= mid:
        result += 1

print(result)
