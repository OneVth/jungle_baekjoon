import sys

input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))
q = []

cnt = 0
for i in range(k):
    if seq[i] in q:
        continue

    if len(q) < n:
        q.append(seq[i])
        continue

    farthest = -1
    target_device = -1
    for device in q:
        next_use = k
        for j in range(i + 1, k):
            if seq[j] == device:
                next_use = j
                break
        
        if next_use > farthest:
            farthest = next_use
            target_device = device

    q.remove(target_device)
    q.append(seq[i])
    cnt += 1

print(cnt)