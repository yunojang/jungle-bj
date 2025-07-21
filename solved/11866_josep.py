n, k = tuple(map(int, input().split()))
from collections import deque

nums = deque(range(1, n + 1))
removed = []


def shift():
    poped = nums.popleft()
    nums.append(poped)


while nums:
    for _ in range(k - 1):
        shift()
    removed.append(nums.popleft())

print("<" + ", ".join(map(str, removed)) + ">")
