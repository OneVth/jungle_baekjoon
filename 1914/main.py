import sys

sys.setrecursionlimit(10**8)


def move(n: int, src: int, dst: int) -> None:
    mid = 6 - src - dst

    if n > 1:
        move(n - 1, src, mid)

    print(src, dst)

    if n > 1:
        move(n - 1, mid, dst)


n = int(sys.stdin.readline().strip())
print(2**n - 1)

if n <= 20:
    move(n, 1, 3)
