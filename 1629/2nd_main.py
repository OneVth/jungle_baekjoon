import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def pow_recur(a, b, c):
    """a를 b제곱한 값을 c로 나머지 연산한 값을 반환하는 함수입니다."""
    if b == 0:
        return 1
    
    if b == 1:
        return a % c
    
    half = pow_recur(a, b // 2, c)
    result = (half * half) % c

    if b % 2 == 1:
        result = (result * a) % c

    return result


a, b, c = map(int, input().split())

print(pow_recur(a, b, c))