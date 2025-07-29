import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
thres = (n + 1) / 2
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    b, s = tuple(map(int, input().split()))
    graph[b].append((s, True))
    graph[s].append((b, False))


def get_s(i):
    cnt = 0
    stk = [i]
    visited = set([i])
    while stk:
        cur = stk.pop()
        for next, is_big in graph[cur]:
            if not is_big or next in visited:
                continue
            visited.add(next)
            cnt += 1
            stk.append(next)
    return cnt


# i보다 큰 값의 개수를 반환
def get_b(i):
    cnt = 0
    stk = [i]
    visited = set([i])
    while stk:
        cur = stk.pop()
        for next, is_big in graph[cur]:
            if is_big or next in visited:
                continue
            visited.add(next)
            cnt += 1
            stk.append(next)
    return cnt


cnt = 0
for i in range(1, n + 1):
    sc = get_s(i)
    bc = get_b(i)

    if sc >= thres or bc >= thres:
        cnt += 1

print(cnt)
