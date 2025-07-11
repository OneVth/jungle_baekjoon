import sys

score = int(sys.stdin.readline().strip())

grade_table = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

print(grade_table.get(score // 10, 'F'))