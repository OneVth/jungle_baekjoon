import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    s = sys.stdin.readline().split()
    
    command = s[0]
    if command == "push":
        stack.append(s[1])
    elif command == "pop":
        try:
            val = stack.pop()
            print(val)
        except:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)