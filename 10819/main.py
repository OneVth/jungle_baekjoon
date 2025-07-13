import sys
from itertools import permutations

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

max_result = 0
length = len(A)

for perm in permutations(A, length):
    result = 0
    for i in range(length - 1):
        result += abs(perm[i] - perm[i + 1])
    if result > max_result:
        max_result = result

print(max_result)