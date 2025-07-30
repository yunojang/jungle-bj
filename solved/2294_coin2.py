import sys
from collections import deque

input = sys.stdin.readline
n, k = tuple(map(int, input().split()))
coins = set()
for _ in range(n):
    coins.add(int(input()))
coins = sorted(coins)
visited = [False] * (k + 1)

q = deque([(0, 0)])
cnt = -1
while q:
    sum, c = q.popleft()
    if sum == k:
        cnt = c
        break
    for coin in coins:
        next = sum + coin
        if next > k or visited[next]:
            continue
        visited[next] = True
        q.append((next, c + 1))
print(cnt)
