import sys

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())

hor = [0, w]
ver = [0, h]

max_width = 0
max_height = 0

for _ in range(n):
    flag, point = map(int, sys.stdin.readline().split())
    if flag:
        hor.append(point)
    else:
        ver.append(point)

hor.sort()
ver.sort()

for i in range(len(hor) - 1):
    width = hor[i + 1] - hor[i]
    if width > max_width:
        max_width = width

for i in range(len(ver) - 1):
    height = ver[i + 1] - ver[i]
    if height > max_height:
        max_height = height

print(max_width * max_height)
