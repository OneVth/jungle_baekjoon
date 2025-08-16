import sys

input = sys.stdin.readline

n = int(input())
hp_list = list(map(int, input().split()))

def solve(a, b, c):
    if a <= 0 and b <= 0 and c <= 0:
        return 0
    
    a, b, c = max(0, a), max(0, b), max(0, c)

    if (a, b, c) in memo:
        return memo[(a, b, c)]
    
    patterns = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

    min_attacks = float('inf')
    for d1, d2, d3 in patterns:
        min_attacks = min(min_attacks, solve(a - d1, b - d2, c - d3) + 1)

    memo[(a, b, c)] = min_attacks
    return min_attacks

# SCV 개수에 따라 패딩 (최대 3개까지)
while len(hp_list) < 3:
    hp_list.append(0)

memo = dict()

print(solve(hp_list[0], hp_list[1], hp_list[2]))
