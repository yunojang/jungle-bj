import sys

inputs = sys.stdin.readlines()

n = int(inputs[0])
sizes = list(map(lambda line: tuple(map(int, line.split(" "))), inputs[1:]))

ranks = []
for kg, h in sizes:
    big_cnt = 0

    for d_kg, d_h in sizes:
        if d_kg > kg and d_h > h:
            big_cnt += 1
    ranks.append(big_cnt + 1)

print(" ".join(map(str, ranks)))
