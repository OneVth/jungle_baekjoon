import sys

sys.setrecursionlimit(10**8)

def modulus(num, n, mod):
    """
    num을 n제곱한 값을 mod로 나머지 연산한 결과를 반환하는 함수입니다.
    나머지 연산 공식 (a * b) % c == ((a % c) * (b % c)) % c를 활용합니다.
    """
    if n == 0:
        return 1
    
    half = modulus(num, n // 2, mod)
    result = (half * half) % mod

    if n % 2 == 1:
        result = (result * (num % mod)) % mod
    
    return result

a, b, c = map(int, sys.stdin.readline().split())

print(modulus(a, b, c))