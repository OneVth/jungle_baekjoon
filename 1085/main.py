import sys

x, y, w, h = map(int, sys.stdin.readline().split())

min = int(1e9)

lines = [x, y, w - x, h - y]

for line in lines:
    if min > line:
        min = line

print(min)