import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[int(c) for c in input().strip()] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()
direction = [-1, 1]
distance = 1

q.append((0, 0, distance))
visited[0][0] = True
while q:
    x, y, d = q.popleft()
    if x == n - 1 and y == m - 1:
        print(d)
        break
    
    # 현재 위치의 상/하 판단
    for dy in direction:
        new_y = y + dy
        if new_y >= 0 and new_y < m:
            if adj[x][new_y] == 1:
                if not visited[x][new_y]:
                    visited[x][new_y] = True
                    q.append((x, new_y, d + 1))

    # 현재 위치의 좌/우 판단
    for dx in direction:
        new_x = x + dx
        if new_x >= 0 and new_x < n:
            if adj[new_x][y] == 1:
                if not visited[new_x][y]:
                    visited[new_x][y] = True
                    q.append((new_x, y, d + 1))