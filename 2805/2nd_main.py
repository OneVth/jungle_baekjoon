import sys

input = sys.stdin.readline

n, m = map(int, input().split())

heights = list(map(int, input().split()))
max_height = max(heights)

start = 0
end = max_height
result = 0

while start <= end:
    mid = (start + end) // 2
    segments = [heights[i] - mid if heights[i] > mid else 0 for i in range(n)]
    
    sum_segment = sum(segments)
    
    # m 이상이면 더 높은 높이 시도
    if sum_segment >= m:
        result = mid
        start = mid + 1
    else:   # m 미만이면 더 낮은 높이 시도
        end = mid - 1

print(result)