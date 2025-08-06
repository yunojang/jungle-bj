import sys
from collections import deque

input = sys.stdin.readline
n, m = tuple(map(int, input().split()))

st = []

for _ in range(m):
    st.append(int(input()))

visited = set([(0, 0)])
q = deque([(1, 0, 0)])

res = -1
while q:
    l, p, cnt = q.popleft()
    if l == n:
        res = cnt
        break
    for i in range(3):
        d = p + (i - 1)
        next = l + d
        if d < 1 or (next in st) or ((next, d) in visited):
            continue
        visited.add((next, d))
        q.append((next, d, cnt + 1))

print(res)


cur = 1
i = 1
while True:
    cur += i
    i += 1
    print(cur)
    if cur > 10000:
        print(i)
        break
