import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    h = int(sys.stdin.readline())
    
    while stack and stack[-1] <= h:
        stack.pop()

    stack.append(h)

print(len(stack))