import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    candidates = []
    for _ in range(n):
        resume, interview = map(int, input().split())
        candidates.append((resume, interview))

    candidates.sort()

    count = 1
    best_interview = candidates[0][1]

    for i in range(1, n):
        if candidates[i][1] < best_interview:
            count += 1
            best_interview = candidates[i][1]

    print(count)
