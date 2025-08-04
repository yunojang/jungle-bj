import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


def lower_bound(arr, v, s, e):
    if s >= e:
        return s
    mid = (s + e) // 2
    if arr[mid] >= v:
        return lower_bound(arr, v, s, mid)
    else:
        return lower_bound(arr, v, mid + 1, e)


lis = []
for num in nums:
    if not lis or lis[-1] < num:
        lis.append(num)
    else:
        i = lower_bound(lis, num, 0, len(lis))
        lis[i] = num

print(len(lis))
