import sys

sys.setrecursionlimit(10*8)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

input = sys.stdin.readline

v, e = map(int, input().split())

parent = [i for i in range(v + 1)]
rank = [0] * (v + 1)
result = 0
edge_count = 0

edges = []
for _ in range(e):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: x[2])

for a, b, cost in edges:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        result += cost
        edge_count += 1
        if edge_count == v - 1:
            break

print(result)