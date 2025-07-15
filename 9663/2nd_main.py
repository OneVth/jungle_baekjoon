import sys

sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

flag_a = [False] * n
flag_b = [False] * (2 * n - 1)
flag_c = [False] * (2 * n - 1)

pos = [0] * n

result = 0


def set(i: int) -> None:
    global result
    for j in range(n):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + (n - 1)]:
            pos[i] = j
            if i == n - 1:
                result += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = False


set(0)
print(result)
