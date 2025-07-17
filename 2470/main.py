import sys

n = int(sys.stdin.readline())

values = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = n - 1

min = int(10e9)
ans = [0] * 2   # 출력할 용액의 특성값
while start < end:
    temp = values[start] + values[end]
    if abs(min) > abs(temp):
        min = temp
        ans[0] = values[start]
        ans[1] = values[end]
    
    if temp == 0:
        break

    if temp > 0:
        end -= 1
    else:
        start += 1


print(ans[0], ans[1])
