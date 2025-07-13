import sys

n = int(sys.stdin.readline().strip())

words = set()
table = [[] for _ in range(50)]

for _ in range(n):
    w = sys.stdin.readline().strip()
    words.add(w)

for w in words:
    table[len(w) - 1].append(w)

result = []

for i in range(50):
    if table[i]:
        table[i].sort()
        result.extend(table[i])

for w in result:
    print(w)