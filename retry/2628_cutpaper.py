import sys

input = sys.stdin.readline

w, h = list(map(int, input().split()))
n = int(input())
cuts = [list(map(int, input().split())) for _ in range(n)]
x_cuts, y_cuts = [0, h], [0, w]


def max_gap(cuts):
    cuts.sort()
    return max(b - a for a, b in zip(cuts, cuts[1:]))


for is_y, pos in cuts:
    (y_cuts if is_y else x_cuts).append(pos)

print(max_gap(x_cuts) * max_gap(y_cuts))
