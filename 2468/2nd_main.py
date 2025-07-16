import sys

from collections import deque

def bfs(x: int, y: int, h: int) -> None:
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        while q:
            cx, cy = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and height_table[nx][ny] > h:
                        q.append((nx, ny))
                        visited[nx][ny] = True


n = int(sys.stdin.readline())

height_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_height = 0
for i in range(n):
    max_height = max(max(height_table[i]), max_height)

max_safe = 0

for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and height_table[i][j] > h:
                safe_area += 1
                bfs(i, j, h)

    max_safe = max(max_safe, safe_area)

print(max_safe)
