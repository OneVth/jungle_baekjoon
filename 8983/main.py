import sys
import bisect


def closest_idx(lst: list, val: int) -> int:
    """list인 lst의 요소 중 val와 가장 가까운 요소의 인덱스를 반환하는 함수입니다"""
    idx = bisect.bisect_left(lst, val)
    if idx >= len(lst):
        idx = len(lst) - 1

    if idx > 0:
        idx = idx - 1 if abs(lst[idx - 1] - val) < abs(lst[idx] - val) else idx

    return idx


n, m, l = map(int, sys.stdin.readline().split())
human_pos = sorted(list(map(int, sys.stdin.readline().split())))
animal_pos = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

cnt = 0
for i in range(m):
    # 동물의 위치와 가장 가까운 사대의 인덱스 구하기
    idx = closest_idx(human_pos, animal_pos[i][0])

    # 사대와 동물 사이의 거리 구하기
    length = abs(human_pos[idx] - animal_pos[i][0]) + animal_pos[i][1]

    # 위에서 구한 거리가 사정거리 l 내부면 cnt 증가
    if length <= l:
        cnt += 1

print(cnt)
