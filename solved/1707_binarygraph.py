import sys

input = sys.stdin.readline
k = int(input())

for _ in range(k):
    n, edg = tuple(map(int, input().split()))
    graph = {i: [] for i in range(1, n + 1)}
    starts = []

    for _ in range(edg):
        u, v = tuple(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
        starts.append(u)

    valid_b = True
    a_set = set()
    b_set = set()
    for i in starts:
        if (i in a_set) or (i in b_set):
            continue
        stk = [(i, True)]
        while stk:
            cur, is_a = stk.pop()
            s = a_set if is_a else b_set
            rs = b_set if is_a else a_set

            if cur in rs:
                valid_b = False
                break
            s.add(cur)

            for adj in graph[cur]:
                if (adj in a_set) or (adj in b_set):  # visited
                    continue
                stk.append((adj, not is_a))
    print("YES" if valid_b else "NO")
