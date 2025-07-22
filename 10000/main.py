import sys
input = sys.stdin.readline

n = int(input())

points = []
for _ in range(n):
    c, r = list(map(int, input().split()))
    points.append(["L", c - r])
    points.append(["R", c + r])

# 좌표 기준 정렬
# x[1]은 오름차순, x[0]은 내림차순(R-L)으로 정렬
points.sort(key=lambda x: (-x[1], x[0]), reverse=True)

stack = []
area = 1

for point in points:
    if point[0] == "L":
        # 왼쪽 끝인 경우
        stack.append(point)
    else:
        # 오른쪽 끝인 경우
        inner_width = 0

        while stack:
            prev = stack.pop()

            # 원의 너비를 계산 후 stack에 추가
            if prev[0] == "L":
                width = point[1] - prev[1]

                # 내부에 있는 원들의 너비 합산이 현재 원의 너비와 일치하는지 확인
                if width == inner_width:
                    area += 2
                else:
                    area += 1

                stack.append(["C", width])
                break
                
            # 내부에 원이 있으면 해당 원의 너비를 누적
            elif prev[0] == "C":
                inner_width += prev[1]

print(area)