n, s = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))

cnt = 0


def sum(sum_v=0, start=0):
    global cnt

    if sum_v == s and start != 0:
        cnt += 1

    if start == n:
        return

    for i in range(start, n):
        sum(sum_v + nums[i], i + 1)


sum()
print(cnt)
