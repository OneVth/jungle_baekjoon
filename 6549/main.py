# 히스토그램의 최대 넓이를 구하는 코드입니다.
import sys

sys.setrecursionlimit(10**8)

def get_area(hist, start, end):
    if start == end:
        return hist[start]
    
    mid = (start + end) // 2
    left_area = get_area(hist, start, mid)
    right_area = get_area(hist, mid + 1, end)
    cross_area = get_cross_area(hist, start, mid, end)

    return max(left_area, right_area, cross_area)


def get_cross_area(hist, start, mid, end):
    left = mid
    right = mid + 1
    height = min(hist[left], hist[right])
    max_area = height * 2

    while start < left or right < end:
        if right < end and (left == start or hist[left - 1] < hist[right + 1]):
            right += 1
            height = min(height, hist[right])
        else:
            left -= 1
            height = min(height, hist[left])
        max_area = max(max_area, height * (right - left + 1))

    return max_area

lst = list(map(int, sys.stdin.readline().split()))
while lst[0] != 0:
    hist = lst[1:]
    max_area = get_area(hist, 0, lst[0] - 1)

    print(max_area)
    lst = list(map(int, sys.stdin.readline().split()))