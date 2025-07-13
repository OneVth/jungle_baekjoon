import sys
sys.setrecursionlimit(10**8)

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

n = int(sys.stdin.readline().strip())

print(factorial(n))