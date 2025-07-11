import sys

a, b = map(int, sys.stdin.read().split())

print(a * (b % 10))
print(a * (b % 100 // 10))
print(a * (b // 100))
print(a * b)