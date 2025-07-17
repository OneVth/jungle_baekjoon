import sys

n, m = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

end = max(trees)
start = 0
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum([trees[i] - mid if trees[i] - mid > 0 else 0 for i in range(n)])

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
