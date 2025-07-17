import sys

n, m = map(int, sys.stdin.readline().split())

houses = []

for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()

start = 1
end = houses[-1] - houses[0]    # 최대 길이

while start <= end:
    p = 0   # 0 position에 공유기를 설치하고 시작
    router_cnt = m - 1
    mid = (end + start) // 2

    for i in range(1, n):
        if houses[i] - houses[p] >= mid:
            router_cnt -= 1
            p = i


        if router_cnt <= 0:
            result = mid
            start = mid + 1
            break

    if router_cnt > 0:
        end = mid - 1

print(result)