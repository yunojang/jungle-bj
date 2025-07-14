n = int(input())

c = [0]


def queen(used_cols, used_dialog1, used_dialog2):
    row = len(used_cols)
    if row == n:
        c[0] += 1
        return

    for col in range(n):
        if col in used_cols or row + col in used_dialog1 or row - col in used_dialog2:
            continue

        used_cols.add(col)
        used_dialog1.add(row + col)
        used_dialog2.add(row - col)
        queen(used_cols, used_dialog1, used_dialog2)
        used_cols.remove(col)
        used_dialog1.remove(row + col)
        used_dialog2.remove(row - col)


queen(set(), set(), set())

print(c[0])
