import sys

score = int(sys.stdin.readline())
score_table = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']

print(score_table[score // 10])