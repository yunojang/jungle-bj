import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
lines = inputs[1:]


def get_score(results):
    score = 0
    scores = [0] * len(results)
    for i in range(len(results)):
        if results[i] == "O":
            scores[i] = (scores[i - 1] if i > 0 else 0) + 1
    for v in scores:
        score += v
    return score


for line in lines:
    print(get_score(line))
