import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    max_heap = []
    min_heap = []
    count = defaultdict(int)  # 각 값의 유효한 개수 추적

    for _ in range(n):
        operation, value = input().split()
        value = int(value)

        if operation == "I":
            heapq.heappush(max_heap, -value)
            heapq.heappush(min_heap, value)
            count[value] += 1
        else:
            if count:  # 큐가 비어있지 않으면
                if value == -1:
                    # 유효하지 않은 원소들 제거
                    while min_heap and count[min_heap[0]] == 0:
                        heapq.heappop(min_heap)
                    if min_heap:
                        min_val = heapq.heappop(min_heap)
                        count[min_val] -= 1
                else:
                    while max_heap and count[-max_heap[0]] == 0:
                        heapq.heappop(max_heap)
                    if max_heap:
                        max_val = -heapq.heappop(max_heap)
                        count[max_val] -= 1

    # 최종 결과 계산 시에도 유효하지 않은 원소들 제거
    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    
    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
