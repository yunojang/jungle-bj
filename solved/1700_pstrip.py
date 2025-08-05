import sys

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
ps = list(map(int, input().split()))

plug = ps[0:n]
cnt = 0
for i in range(n, k):
    cur = ps[i]
    if cur in plug:
        continue
    else:
        candi = (0, None)
        for p in plug:
            ni = ps.index(p, i + 1) if p in ps[i + 1 :] else float("inf")
            if candi[0] < ni:
                candi = (ni, p)
        plug.remove(candi[1])
        cnt += 1
        plug.append(cur)

print(cnt)
