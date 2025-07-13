import sys
inputs = sys.stdin.readlines()
n = int(inputs[0])
lines = inputs[1:]

for line in lines:
    t, s = line.split(" ")
    res = []
    for c in s:
        if c == '\n':
            continue
        for _ in range(int(t)):
            res.append(c)
    print("".join(res))