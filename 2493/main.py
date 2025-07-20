import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

stack = []
result = [0] * n

for i in range(n):

    # stack에 현재 탑보다 낮은 탑을 제거해가며 가장 높은 왼쪽 탑을 찾는다
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1] + 1  # 1-based

    # stack에 현재 기둥의 인덱스를 저장합니다.
    stack.append(i)

print(*result)
