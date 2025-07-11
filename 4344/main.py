import sys

n = int(sys.stdin.readline())

for _ in range(n):
    exam_info = list(map(int, sys.stdin.readline().split()))
    count = exam_info[0]
    score_list = exam_info[1:]
    
    avg = sum(score_list) / count
    above_avg = sum(1 for s in score_list if s > avg)

    rate = above_avg / count * 100
    print(f'{rate:.3f}%') 