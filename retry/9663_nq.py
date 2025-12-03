import sys

n = int(sys.stdin.readline())
col_visited = [False] * n
cnt = 0


def search(count=0):
    global cnt
    if count == n:
        cnt += 1
        return

    for col in range(n):
        next = count + 1
        l, r = next - col, next + col
        if col_visited[col]:
            continue
        col_visited[col] = True
        search(next)
        col_visited[col] = False


search(0)
print(cnt)
