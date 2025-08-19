import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
hp_list = list(map(int, input().split()))

# SCV 개수에 따라 패딩 (최대 3개까지)
while len(hp_list) < 3:
    hp_list.append(0)

visited = set()
queue = deque()  
queue.append((hp_list[0], hp_list[1], hp_list[2], 0))   # (a, b, c, 공격횟수)
visited.add((hp_list[0], hp_list[1], hp_list[2]))

patterns = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

while queue:
    a, b, c, attacks = queue.popleft()

    if a <= 0 and b <= 0 and c <= 0:
        print(attacks)

    for d1, d2, d3 in patterns:
        next_a = max(0, a - d1)
        next_b = max(0, b - d2)
        next_c = max(0, c - d3)

        if (next_a, next_b, next_c) not in visited:
            visited.add((next_a, next_b, next_c))
            queue.append((next_a, next_b, next_c, attacks + 1))

    
