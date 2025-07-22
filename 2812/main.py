import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

stack = []
erased = 0
for i in range(n):
    if not stack:
        stack.append(s[i])
    else:
        while stack and int(stack[-1]) < int(s[i]) and erased < k:
            stack.pop()
            erased += 1
        stack.append(s[i])

# k개보다 적게 지웠을 경우 후처리
if erased < k:
    left = erased - k
    stack = stack[:left]

print(''.join(stack))