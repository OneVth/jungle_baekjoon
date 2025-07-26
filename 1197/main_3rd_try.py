import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def find_parent(v):
    if parent[v] != v:
        parent[v] = find_parent(parent[v])
    return parent[v]


def union(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)
    if root_a != root_b:
        parent[root_b] = root_a


v, e = map(int, input().split())

parent = [i for i in range(v + 1)]

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
added = 0
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost
        added += 1

    if added >= (v - 1):
        break

print(result)
