# dp 풀이
# dp[pos][jump] - pos에 jump 거리로 도착 했을 때 최소 이동
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
stone = set(int(input()) for _ in range(m))

max_jump = int((2 * n) ** 0.5) + 2
dp = [[float("inf")] * (max_jump + 1) for _ in range(n + 1)]
dp[1][0] = 0

for pos in range(1, n + 1):
    for x in range(max_jump + 1):
        if dp[pos][x] == float("inf"):  # pos에 x점프로 도달한적 없음
            continue
        for nj in (x - 1, x, x + 1):
            np = pos + nj
            if 1 <= np and np <= n and np not in stone:
                dp[np][nj] = min(dp[np][nj], dp[pos][x] + 1)

print(dp)
result = min(dp[n])
print(result if result != float("inf") else -1)
