import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
lines = inputs[1:]


def over_avg_rate(n, scores):
    avg = sum(scores) / n
    over = 0
    for score in scores:
        if score > avg:
            over += 1
    return (over / n) * 100


for line in lines:
    n, *scores = tuple(map(int, line.split(" ")))
    print(f"{over_avg_rate(n, scores):.3f}%")
