import sys

input = sys.stdin.readline

w, h = list(map(int, input().split()))
n = int(input())
cuts = [list(map(int, input().split())) for _ in range(n)]
x_cuts = [0, h]
y_cuts = [0, w]

for is_y, pos in cuts:
    if is_y:
        y_cuts.append(pos)
    else:
        x_cuts.append(pos)
x_cuts.sort()
y_cuts.sort()

xmax = 0
ymax = 0
for x1, x2 in zip(x_cuts, x_cuts[1:]):
    xmax = max(xmax, x2 - x1)
for y1, y2 in zip(y_cuts, y_cuts[1:]):
    ymax = max(ymax, y2 - y1)


print(xmax * ymax)
