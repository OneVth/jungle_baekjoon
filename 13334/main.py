import sys
import heapq

n = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
l = int(sys.stdin.readline())

# x[0] 와 x[1] 중 작은 수가 x[0] 자리에 오도록 정렬
lines = [tuple(sorted(line)) for line in lines]

# 끝점을 기준으로 정렬
lines.sort(key=lambda x: x[1])

pq = []
result = 0
for start, end in lines:
    if end - start > l:
        continue

    heapq.heappush(pq, start)
    
    # l 길이 조건 만족하는 선분만 유지
    while pq and pq[0] < end - l:
        heapq.heappop(pq)

    result = max(result, len(pq))

print(result)
