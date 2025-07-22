import sys

s = sys.stdin.readline().strip()

stack = []
result = 0
tmp = 1
for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break

        # s[i - 1] (직전 괄호)가 현재 괄호와 대응하는 여는 괄호일 경우만 result에 tmp를 더한다.
        if s[i - 1] == '(':
            result += tmp
        stack.pop()
        tmp //= 2    # tmp 초기화
    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        
        # s[i - 1] (직전 괄호)가 현재 괄호와 대응하는 여는 괄호일 경우만 result에 tmp를 더한다.
        if s[i - 1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3    # tmp 초기화

if stack:
    result = 0
print(result)