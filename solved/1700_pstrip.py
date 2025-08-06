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
        last_idx = -1
        out = None

        for p in plug:
            try:
                idx = ps.index(p, i + 1)
            except ValueError:
                idx = float("inf")
            if idx > last_idx:
                last_idx = idx
                out = p

        plug.remove(out)
        plug.append(cur)
        cnt += 1

print(cnt)
