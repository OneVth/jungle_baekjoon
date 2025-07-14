import sys
from collections import deque

n = int(sys.stdin.readline())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, table))

result = 0


def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and table[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))


for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    result = max(result, cnt)

print(result)
