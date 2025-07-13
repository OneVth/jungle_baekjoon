import sys

n = int(sys.stdin.readline().strip())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

for i in range(len(arr)):
    print(arr[i])