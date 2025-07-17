import sys

n = int(sys.stdin.readline())
table = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())

target = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    pr = n - 1
    pl = 0
    pc =  (pr + pl) // 2

    while True:
        if table[pc] == target[i]:
            print(1)
            break

        if table[pc] > target[i]:
            pr = pc - 1
            pc = (pl + pr) // 2
        elif table[pc] < target[i]:
            pl = pc + 1
            pc = (pl + pr) // 2

        if pr < pl:
            print(0)
            break