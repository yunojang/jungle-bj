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


temp = []
for num in nums:
    i = lower_bound(temp, num, 0, len(temp))
    if i == len(temp):
        temp.append(num)
    else:
        temp[i] = num

print(len(temp))
