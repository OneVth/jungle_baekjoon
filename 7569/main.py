import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split())

box = [[] for _ in range(h)]

for i in range(h):
    for _ in range(m):
        box[i].append(list(map(int, input().split())))

q = deque()
for k in range(h):
    for j in range(m):
        for i in range(n):
            if box[k][j][i] == 1:
                q.append((k, j, i, 0))

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
result = 0
while q:
    z, y, x, d = q.popleft()
    result = max(d, result)

    for dz, dy, dx in directions:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = 1
                q.append((nz, ny, nx, d + 1))


for k in range(h):
    for j in range(m):
        if not all(box[k][j]):
            result = -1
            break

print(result)
