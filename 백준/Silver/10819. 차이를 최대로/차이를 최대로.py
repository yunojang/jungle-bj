n = int(input())
list = list(map(int, input().split(" ")))

max_sum = [0]


def per(path, visited, prev_v=0, d_sum=0):
    if len(path) == n:
        max_sum[0] = max(max_sum[0], d_sum)
        return

    for i in range(len(list)):
        if visited[i]:
            continue

        visited[i] = True
        per(
            path + [list[i]],
            visited,
            list[i],
            d_sum + (abs(prev_v - list[i]) if path else 0),
        )
        visited[i] = False


per([], [False for _ in range(n)])
print(max_sum[0])
