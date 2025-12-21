# n, m, k = tuple(map(int, input().split()))
# nums = [int(input()) for _ in range(n)]

# for _ in range(m + k):
#     oper, n1, n2 = tuple(map(int, input().split()))
#     if oper == 1:
#         nums[n1 - 1] = n2
#     else:
#         print(sum(nums[n1 - 1 : n2]))


import sys

input = sys.stdin.readline


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.t[i] += delta
            i += i & -i

    def prefix(self, i):
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.prefix(r) - self.prefix(l - 1)


n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]  # 1-based
fw = Fenwick(n)
for i in range(1, n + 1):
    fw.update(i, nums[i])

out = []
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:  # update
        diff = c - nums[b]
        nums[b] = c
        fw.update(b, diff)
    else:  # query
        out.append(str(fw.range_sum(b, c)))

sys.stdout.write("\n".join(out))
