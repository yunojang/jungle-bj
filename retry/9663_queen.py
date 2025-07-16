n = int(input())

count = [0]


def queen(depth, cols, dialog1, dialog2):
    if depth == n:
        count[0] += 1
        return

    for col in range(n):
        if col in cols:
            continue

        if depth + col in dialog1 or depth - col in dialog2:
            continue

        dialog1.add(depth + col)
        dialog2.add(depth - col)
        queen(depth + 1, cols + [col], dialog1, dialog2)
        dialog1.remove(depth + col)
        dialog2.remove(depth - col)


queen(0, [], set(), set())
print(count[0])
