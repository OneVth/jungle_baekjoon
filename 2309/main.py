import sys
from itertools import combinations

heights = [int(sys.stdin.readline()) for _ in range(9)]

for comb in combinations(heights, 7):
    if sum(comb) == 100:
        for h in sorted(comb):
            print(h)
        break