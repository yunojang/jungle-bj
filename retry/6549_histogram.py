import sys
lines = sys.stdin.readlines()

def get_max_rect(n, blocks):
    max_rect = 0
    mm = []
    for i in range(n):
        while mm and blocks[mm[-1]] > blocks[i]:
            poped = mm.pop()
            width = i - mm[-1] - 1 if mm else i
            max_rect = max(max_rect, width * blocks[poped])
        mm.append(i)
    return max_rect
        

for line in lines:
    if line == '0\n':
        break
    n, *blocks = list(map(int,line.split(" ")))
    print(get_max_rect(n+1,blocks+[0]))
