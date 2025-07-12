import sys

def is_hansu(s: int) -> bool:
    s = str(s)
    d = int(s[0]) - int(s[1])
    for i in range(1, len(s) - 1):
        if (int(s[i]) - int(s[i + 1])) != d:
            return False
        
    return True


N = int(sys.stdin.readline().strip())

result = 99
if N <= result:
    result = N

for i in range(100, N + 1):
    if is_hansu(i):
        result += 1

print(result)