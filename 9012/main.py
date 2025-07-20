import sys

n = int(sys.stdin.readline())

for _ in range(n):
    stack = []
    
    line = sys.stdin.readline().strip()
    for c in line:
        if c == ')':
            val = 0
            try:
                val = stack.pop()
            except:
                print('NO')
                break

            if val != '(':
                print('NO')
                break
        else:
            stack.append(c)
    else:
        if stack:
            print('NO')
        else:
            print('YES')