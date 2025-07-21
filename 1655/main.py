# 우선순위 큐를 활용해서 중앙값을 구하는 문제입니다.

import sys
import heapq

n = int(sys.stdin.readline())

min_heap = []
max_heap = []
mid = -10001
for _ in range(n):
    tmp = int(sys.stdin.readline())

    # 현재 mid(중앙값)보다 크거나 같은 입력이 들어오면 min_heap에 push
    if mid <= tmp:
        heapq.heappush(min_heap, tmp)
    else:
        heapq.heappush(max_heap, -tmp)

    # min_heap과 max_heap의 크기를 비교하여 2이상 차이날 경우 재배열합니다.
    if len(min_heap) - len(max_heap) >= 2:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) - len(min_heap) >= 2:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # max_heap의 요소가 더 많거나 같은 경우, max_heap의 첫 요소가 중앙값입니다.
    if len(max_heap) >= len(min_heap):
        mid = -max_heap[0]
    else:
        mid = min_heap[0]

    print(mid)
