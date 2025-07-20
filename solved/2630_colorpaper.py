# n * n 크기 종이가 모두 같은 색 종이라면,
import sys

n = int(sys.stdin.readline())
paper = []

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

cnt = [0, 0]


# sy,sx부터 n거리의 정사각형이 색이 같으면, cnt를 증가한다.
def color_count(n, sy=0, sx=0):
    cur_color = paper[sy][sx]
    same = True
    for y in range(sy, sy + n):
        for x in range(sx, sx + n):
            same = same and (cur_color == paper[y][x])

    if same:
        cnt[1 if cur_color else 0] += 1
        return

    unit = n // 2
    color_count(unit, sy, sx)
    color_count(unit, sy, sx + unit)
    color_count(unit, sy + unit, sx)
    color_count(unit, sy + unit, sx + unit)


color_count(n)
for c in cnt:
    print(c)
