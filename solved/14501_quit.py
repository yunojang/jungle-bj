import sys

input = sys.stdin.readline
n = int(input())
plans = [tuple(map(int, input().split())) for _ in range(n)]


best = 0


def search_job(start, total=0):
    global best
    best = max(total, best)

    if start == n:
        return

    for i in range(start, n):
        day, earn = plans[i]
        if (i + day) > n:
            continue
        search_job(i + day, total + earn)


search_job(0)
print(best)
