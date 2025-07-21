import sys

sys.setrecursionlimit(10**6)
n = sys.stdin.readline()
circles = list(map(lambda l: tuple(map(int, l.split())), sys.stdin.readlines()))
circles.sort(key=lambda c: (-c[1], c[0]))


class Tree:
    def __init__(self, circle):
        x, r = circle
        self.s = x - r
        self.e = x + r
        self.children = []

    def is_contain(self, circle):
        x, r = circle
        s, e = x - r, x + r
        return s >= self.s and e <= self.e

    def append(self, circle):
        for child in self.children:
            if child.is_contain(circle):
                child.append(circle)
                break
        else:
            self.children.append(Tree(circle))

    def count_area(self):
        cnt = 1

        child_len = 0
        for child in self.children:
            child_len += child.e - child.s
            cnt += child.count_area()
        if child_len == self.e - self.s:
            cnt += 1
        return cnt

    def __str__(self):
        return str(len(self.children))


trees = []

for circle in circles:
    # make trees
    for tree in trees:
        if tree.is_contain(circle):
            tree.append(circle)
            break
    else:
        trees.append(Tree(circle))

# count area
s = 0
for t in trees:
    s += t.count_area()

# 외부영역 + 1
print(s + 1)
