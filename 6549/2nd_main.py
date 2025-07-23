import sys

sys.setrecursionlimit(10**8)

def get_max_across_rec(heights, left, mid, right):
    i = mid
    j = mid + 1

    height = min(heights[i], heights[j])
    max_area = height * 2

    while i > left or j < right:
        if i == left:
            j += 1
            height = min(heights[j], height)
        elif j == right:
            i -= 1
            height = min(heights[i], height)
        else:
            if heights[i - 1] > heights[j + 1]:
                i -= 1
                height = min(heights[i], height)
            else:
                j += 1
                height = min(heights[j], height)

        current_area = height * (j - i + 1)
        max_area = max(max_area, current_area)
    return max_area


def get_max_rec_recur(heights, left, right):
    if left == right:
        return heights[left]

    mid = (left + right) // 2
    left_max = get_max_rec_recur(heights, left, mid)
    right_max = get_max_rec_recur(heights, mid + 1, right)
    across_max = get_max_across_rec(heights, left, mid, right)

    return max(left_max, right_max, across_max)


def get_max_rec(heights):
    return get_max_rec_recur(heights, 0, len(heights) - 1)


input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    n = line[0]
    heights = line[1:]

    result = get_max_rec(heights)
    print(result)
