import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) # Path compression
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False


case_num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    has_cycle = [False] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        if not union(parent, rank, u, v):
            # 사이클 발생
            root = find(parent, u)
            has_cycle[root] = True

    
    # 트리 개수 계산
    trees = set()
    for i in range(1, n + 1):
        root = find(parent, i)
        if not has_cycle[root]:
            trees.add(root)

    tree_count = len(trees)
    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")

    case_num += 1