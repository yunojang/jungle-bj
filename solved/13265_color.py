import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = tuple(map(int, input().split()))
    starts = []
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = tuple(map(int, input().split()))
        starts.append(u)
        graph[u].append(v)
        graph[v].append(u)
    set_a = set()
    set_b = set()
    is_possible = True
    for s in starts:
        # visited continue
        if (s in set_a) or (s in set_b):
            continue
        q = deque([(s, True)])
        while q:
            cur, is_a = q.popleft()
            s = set_a if is_a else set_b
            rs = set_b if is_a else set_a
            if cur in rs:
                is_possible = False
                break
            s.add(cur)
            for adj in graph[cur]:
                if (adj in set_a) or (adj in set_b):
                    continue
                q.append((adj, not is_a))

    print("possible" if is_possible else "impossible")
