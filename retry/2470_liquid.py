# arr의 s,e 내에서 n과 유사한 값을 찾는함수
def lower_bound(arr, n, s, e):
    if s >= e:
        return s

    mid = (s + e) // 2
    if arr[mid] >= n:
        return lower_bound(arr, n, s, mid)
    else:
        return lower_bound(arr, n, mid + 1, e)


# 1,2,4,5,6 -> 3을 구할라해 -> 크든 작든 3과 가장 유사한

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

min_abs = float("inf")
min_v = None

for i in range(n):
    v = nums[i]
    lb = lower_bound(nums, -v, i + 1, n)

    candidates = []
    if lb < n:
        candidates.append(nums[lb])
    if lb - 1 >= i + 1:
        candidates.append(nums[lb - 1])

    for sim in candidates:
        if abs(v + sim) < min_abs:
            min_abs = abs(v + sim)
            min_v = (v, sim)

# min_v.sort()
a, b = min_v
print(a, b)
