import sys


def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def brute_force(pts):
    min_d = float("inf")
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            min_d = min(min_d, dist_sq(pts[i], pts[j]))
    return min_d


def closest_rec(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)

    mid = n // 2
    mid_x = px[mid][0]

    Qx = px[:mid]
    Rx = px[mid:]
    Qy = [p for p in py if p[0] <= mid_x]
    Ry = [p for p in py if p[0] > mid_x]

    d1 = closest_rec(Qx, Qy)
    d2 = closest_rec(Rx, Ry)
    d = min(d1, d2)

    strip = [p for p in py if abs(p[0] - mid_x) ** 2 < d]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = min(d, dist_sq(strip[i], strip[j]))
    return d


def closest_pair(points):
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_rec(px, py)


n = int(sys.stdin.readline())

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(closest_pair(points))
