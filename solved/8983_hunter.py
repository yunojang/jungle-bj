import sys

m, n, l = list(map(int, sys.stdin.readline().split()))
fire_points = list(map(int, sys.stdin.readline().split()))
animals = list(map(lambda l: tuple(map(int, l.split())), sys.stdin.readlines()))

fire_points.sort()
cnt = 0

def search_point(x, r, s, e):
    if s>=e:
        return False

    mid = (s+e) // 2
    if x-r <= fire_points[mid] and fire_points[mid] <= x+r:
        return True
    elif fire_points[mid] > x+r:
        return search_point(x, r, s, mid)
    else:
        return search_point(x, r, mid+1, e)

for ax, ay in animals:
    r = l - ay
    if search_point(ax, r, 0, len(fire_points)):
        cnt += 1

print(cnt)

