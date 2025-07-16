import sys

sys.setrecursionlimit(10**8)

def dfs(x: int, y: int, h: int) -> None:
        visited[x][y] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and height_table[nx][ny] > h:
                    dfs(nx, ny, h)


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
                dfs(i, j, h)

    max_safe = max(max_safe, safe_area)

print(max_safe)
