import sys
import heapq

input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    i, f = map(int, input().split())
    meetings.append((i, f))
meetings.sort(key=lambda x: (x[1], x[0]))

last_end = 0
count = 0
for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)

