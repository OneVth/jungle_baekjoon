import sys

def is_prime(a: int) -> bool:
    if a < 2:
        return False
    
    for i in range(2, a):
        if i * i > a:
            break

        if a % i == 0:
            return False
        
    return True

n = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().split()

result = 0
for i in range(n):
    if is_prime(int(arr[i])):
        result += 1
print(result)
