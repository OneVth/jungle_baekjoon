import sys
from collections import deque

input = sys.stdin.readline


def bfs(pos):
    queue = deque([pos])
    x, y = pos
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and mat[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

time = 0
ice = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(m):
        if mat[i][j] != 0:
            ice.append((i, j))

while True:
    if len(ice) == 0:
        time = 0
        break

    melt = [[0] * m for _ in range(n)]
    for x, y in ice:
        sea_count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                sea_count += 1
        melt[x][y] = sea_count

    for x, y in ice:
        mat[x][y] = max(0, mat[x][y] - melt[x][y])

    ice = [(x, y) for x, y in ice if mat[x][y] > 0]
    time += 1

    visited = [[False] * m for _ in range(n)]
    is_connected = True
    connected = 0
    for x, y in ice:
        if not visited[x][y]:
            connected += 1
            if connected > 1:
                is_connected = False
                break
            bfs((x, y))

    if not is_connected:
        break

print(time)
