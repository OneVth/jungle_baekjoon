import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def dfs(vertex):
    for v in adj[vertex]:
        if not color[v]:
            color[v] = -color[vertex]
            if not dfs(v):
                return False
        elif color[vertex] == color[v]:
            return False
    return True

k = int(input())
for _ in range(k):
    n, e = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    color = [0] * (n + 1)
    result = True

    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        if not color[i]:
            color[i] = 1
            result =  dfs(i)
            if not result:
                break

    if result:
        print("YES")
    else:
        print("NO")

    