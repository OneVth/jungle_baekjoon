import sys

input = sys.stdin.readline

n, c = map(int, input().split())

pos = sorted(int(input()) for _ in range(n))

# 최소 인접 거리를 이분 탐색 대상으로 선택
start = 1
end = pos[-1] - pos[0]

result = 0
while start <= end:
    mid = (start + end) // 2

    # 0위치에 첫 번째 공유기를 설치했다고 가정
    k = 1
    set_pos = 0
    for i in range(1, n):

        # 두 pos의 차이가 mid 크기 이상이면 공유기를 설치하고 기준 pos을 최신화
        if pos[i] - pos[set_pos] >= mid:
            k += 1
            set_pos = i

            # c개 이상 설치 했는지 확인
            if k >= c:
                result = mid
                start = mid + 1
                break
    else:
        end = mid - 1

print(result)