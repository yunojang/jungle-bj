import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))


def diff_sum(arr):
    return sum(abs(a - b) for a, b in zip(arr, arr[1:]))


best = 0
picked = [0] * n
used = [False] * n


# depth 부터, 모든 순열 조합을
def search(depth):
    global best
    if depth == n:
        best = max(best, diff_sum(picked))
        return
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        picked[depth] = nums[i]
        search(depth + 1)
        used[i] = False


search(0)
print(best)
