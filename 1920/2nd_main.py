import sys
import bisect

input = sys.stdin.readline

n = int(input())

# 대상 배열을 정렬된 상태로 반환
a = sorted(list(map(int, input().split())))

m = int(input())
target = list(map(int, input().split()))

for i in range(m):
    
    # bisect 모듈을 사용해서 이분 탐색합니다.
    idx = bisect.bisect_left(a, target[i])
    if idx != n and a[idx] == target[i]:
        print(1)
    else:
        print(0)