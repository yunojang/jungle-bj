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


# dp 풀이
# import sys

# input = sys.stdin.readline
# n = int(input())
# t, p = zip(*(map(int, input().split()) for _ in range(n)))

# dp = [0] * (n + 1)  # dp[i]: i번째 날부터 얻을 수 있는 최대 수익
# for i in range(n - 1, -1, -1):
#     skip = dp[i + 1]
#     take = p[i] + dp[i + t[i]] if i + t[i] <= n else 0
#     dp[i] = max(skip, take)

# print(dp[0])
