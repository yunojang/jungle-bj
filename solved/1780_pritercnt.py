import sys
n = int(sys.stdin.readline())
paper = list(map(lambda l: list(map(int, l.split())), sys.stdin.readlines()))

cnt_idx = {-1: 0, 0:1, 1:2}
cnt = [0, 0, 0]

# sy,sx에서 n만큼 크기로, 모두 같으면 카운트 / 다른게 있으면 9등분하여 재귀
def count_paper(n, sy, sx):
    is_same = True
    sig = paper[sy][sx]

    if n == 1:
        cnt[cnt_idx[sig]] += 1
        return
    
    for y in range(n):
        for x in range(n):
            is_same = is_same and paper[sy+y][sx+x] == sig

    if is_same:
        cnt[cnt_idx[sig]] += 1
    else:
        unit = n // 3
        for y in range(3):
            for x in range(3):
                count_paper(unit, sy+y*unit,sx+x*unit)

count_paper(n, 0,0)

for c in cnt:
    print(c)