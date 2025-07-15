import sys

hs = list(map(int, sys.stdin.readlines()))


def print_sort(arr):
    arr.sort()
    for h in arr:
        print(h)


def search(arr, path, sum=0, start=0):
    if sum == 100 and len(path) == 7:
        print_sort(path)
        return True

    for i in range(start, len(arr)):
        if sum + arr[i] > 100:
            continue

        if search(arr, path + [arr[i]], sum + arr[i], i + 1):
            return True


search(hs, [])
