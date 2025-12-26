n, m = tuple(map(int, input().split()))
ns1 = list(map(int, input().split()))
ns2 = list(map(int, input().split()))

res = []
s = set(ns2)
for x in ns1:
    if x not in s:
        res.append(x)

if res:
    print(len(res))
res.sort()
print(" ".join(map(str, res)) if res else 0)
