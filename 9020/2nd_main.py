import sys


def is_prime(a: int) -> bool:
    """소수를 판별하는 함수"""
    if a < 2:
        return False

    for i in range(2, a):
        if i * i > a:
            break

        if a % i == 0:
            return False

    return True


n = int(sys.stdin.readline())

for _ in range(n):
    even = int(sys.stdin.readline())
    half = even // 2
    for i in range(half, -1, -1):
        if is_prime(i) and is_prime(even - i):
            print(i, even - i)
            break
