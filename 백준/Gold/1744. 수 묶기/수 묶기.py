import sys

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]

nega = []
posi = []
isZero = False

for x in nums:
    if x == 0:
        isZero = True
    elif x > 0:
        posi.append(x)
    else:
        nega.append(x)


posi.sort(reverse=True)
nega.sort()

res = 0
for i in range(0, len(posi), 2):
    n1, n2 = posi[i], posi[i + 1] if i < len(posi) - 1 else None
    if n2 == None:
        res += n1
        continue
    if n1 * n2 >= n1 + n2:
        res += n1 * n2
    else:
        res += n1 + n2


for i in range(0, len(nega), 2):
    n1, n2 = nega[i], nega[i + 1] if i < len(nega) - 1 else None
    if n2 == None:
        if not isZero:
            res += n1
        continue
    res += n1 * n2


print(res)
