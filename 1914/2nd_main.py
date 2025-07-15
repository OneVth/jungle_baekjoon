import sys

sys.setrecursionlimit(10**8)


def move(no: int, src: int, dst: int) -> None:
    """n 개의 블록을 src에서 dst로 이동"""
    mid = 6 - src - dst

    if no > 1:
        move(no - 1, src, mid)

    print(src, dst)

    if no > 1:
        move(no - 1, mid, dst)


n = int(sys.stdin.readline())

print(2**n - 1)

if n <= 20:
    move(n, 1, 3)
