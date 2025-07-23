import sys
import bisect

input = sys.stdin.readline

m, n, l = map(int, input().split())
m_pos = sorted(list(map(int, input().split())))
animal_pos = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    idx = bisect.bisect_left(m_pos, animal_pos[i][0])
    if idx == len(m_pos):
        idx -= 1

    if idx > 0:
        # animal_pos에서 x거리가 가장 가까운 사대 찾기
        idx = idx - 1 if abs(m_pos[idx - 1] - animal_pos[i][0]) < abs(m_pos[idx] - animal_pos[i][0]) else idx

    if abs(m_pos[idx] - animal_pos[i][0]) + animal_pos[i][1] <= l:
        cnt += 1

print(cnt)
