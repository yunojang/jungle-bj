import sys

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = 0

for coin in reversed(coins):
    if k == 0:
        break
    if k >= coin:
        cnt += k // coin
        k %= coin

print(cnt)
