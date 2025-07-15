import sys

N, r, c = map(int, sys.stdin.readline().split())

result = 0

while N:
    N -= 1

    if 0 <= r < 2**N and 0 <= c < 2**N:
        continue

    elif 0 <= r < 2**N and 2**N <= c < 2 ** (N + 1):
        c -= 2**N
        result += pow(2**N, 2)

    elif 2**N <= r < 2 ** (N + 1) and 0 <= c < 2**N:
        r -= 2**N
        result += pow(2**N, 2) * 2

    elif 2**N <= r < 2 ** (N + 1) and 2**N <= c < 2 ** (N + 1):
        r -= 2**N
        c -= 2**N
        result += pow(2**N, 2) * 3

    else:
        break


print(result)
