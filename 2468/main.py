import sys

sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, table))

result = 0


def dfs(x, y, h):
    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and table[nx][ny] > h:
                dfs(nx, ny, h)


for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j] > h:
                dfs(i, j, h)
                cnt += 1
    result = max(result, cnt)

print(result)
