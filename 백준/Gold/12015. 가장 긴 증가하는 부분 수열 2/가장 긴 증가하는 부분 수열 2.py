n = int(input())
nums = list(map(int, input().split()))


def lower_bound(arr, v, s, e):
    if s >= e:
        return s

    mid = (s + e) // 2
    if v <= arr[mid]:
        return lower_bound(arr, v, s, mid)
    else:
        return lower_bound(arr, v, mid + 1, e)


min_end = []
for num in nums:
    lb = lower_bound(min_end, num, 0, len(min_end))

    if lb >= len(min_end):
        min_end.append(num)
    else:
        min_end[lb] = num


def lower_bound(arr, v, s, e):
    if s >= e:
        return s

    mid = (s + e) // 2
    if v <= arr[mid]:
        lower_bound(arr, v, s, mid)
    else:
        lower_bound(arr, v, mid + 1, e)


print(len(min_end))
