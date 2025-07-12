import sys
import math

n = 3
operands = []

for _ in range(n):
    operands.append(int(sys.stdin.readline().strip()))

result = math.prod(operands)
result = list(str(result))

for i in range(10):
    print(result.count(str(i)))