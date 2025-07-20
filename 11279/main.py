import sys
import heapq

n = int(sys.stdin.readline())

max_heap = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        try:
            print(-heapq.heappop(max_heap))
        except:
            print(0)
    else:
        heapq.heappush(max_heap, -i)