import sys
inputs = sys.stdin.readlines() 

w, h = list(map(int, inputs[0].split(" ")))
n = int(inputs[1])
cuts = inputs[2:]

xs = []
ys = []
for cut in cuts:
    d, v = tuple(map(int, cut.split(" ")))
    if d == 0:
        xs.append(v)
    else:
        ys.append(v)
    
xs.sort()
ys.sort()

def get_interval(sorted, end):
    prev = 0
    intervals = []
    for v in sorted + [end]:
        intervals.append(v - prev)
        prev = v
    return intervals

mx = max(get_interval(xs, h))
my = max(get_interval(ys, w))

print(mx * my)