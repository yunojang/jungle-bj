x, y, w, h = tuple(map(int, input().split(" ")))

d = min(x, w - x, y, h - y)
print(d)
