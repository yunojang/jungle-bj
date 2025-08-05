import sys

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
ps = list(map(int, input().split()))

plug = []
cnt = 0
for i in range(k):
    cur = ps[i]
    if cur in plug:
        continue
    if len(plug) < n:
        plug.append(cur)
    else:
        plug.sort(
            key=lambda p: ps.index(p, i + 1) if p in ps[i + 1 :] else float("inf")
        )
        plug.pop()
        plug.append(cur)
        cnt += 1

print(cnt)
