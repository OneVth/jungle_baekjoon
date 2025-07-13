import sys

ans = 0
N, r, c = map(int, sys.stdin.readline().split())

while N:
    N -= 1
    if r < 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 0

    elif r < 2**N and c >= 2**N:
        ans += (2**N) * (2**N) * 1
        c -= 2**N

    elif r >= 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 2
        r -= 2**N

    elif r >= 2**N and c >= 2**N:
        ans += (2**N) * (2**N) * 3
        r -= 2**N
        c -= 2**N

print(ans)
