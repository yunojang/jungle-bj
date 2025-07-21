n, k = list(map(int, input().split()))

from collections import deque

d = deque(range(1, n + 1))
removed = []


def shift():
    d.append(d.popleft())


while d:
    for _ in range(k - 1):
        shift()
    removed.append(d.popleft())

print("<" + ", ".join(map(str, removed)) + ">")
