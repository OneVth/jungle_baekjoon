import sys
from itertools import permutations

n = int(sys.stdin.readline())

charge_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cheapest = int(10**9)

for perm in permutations(range(n), n):
    total_cost = 0
    
    for i in range(n - 1):
        cost = charge_table[perm[i]][perm[i + 1]]
        if cost:
            total_cost += cost
        else:
            break
    
    else:
        cost = charge_table[perm[-1]][perm[0]]
        if cost:
            total_cost += cost
            cheapest = min(cheapest, total_cost)
    
print(cheapest)
