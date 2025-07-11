import sys

score = int(sys.stdin.readline().strip())

grade_table = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']

print(grade_table[score // 10])