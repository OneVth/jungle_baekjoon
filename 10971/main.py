import sys
from itertools import permutations

n = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_cost = int(10e9)

for path in permutations(range(n)):
    cost = 0
    valid = True

    for i in range(n - 1):
        src = path[i]
        dst = path[i + 1]
        if W[src][dst] == 0:
            valid = False
            break
        cost += W[src][dst]
    if valid and W[path[-1]][path[0]]:
        cost += W[path[-1]][path[0]]
        min_cost = min(min_cost, cost)

print(min_cost)