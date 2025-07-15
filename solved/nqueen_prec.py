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


# queen(set(), set(), set())

# print(c[0])

c1 = [0]


#  고정위치 n-queen (특정위치에 항상 퀸이 있어야함 (0,0))
def queen1(used_cols, used_dia1, used_dia2):
    row = len(used_cols)
    if row == n:
        c1[0] += 1
        return

    for col in range(n):
        if col in used_cols or row + col in used_dia1 or row - col in used_dia2:
            continue

        used_cols.add(col)
        used_dia1.add(row + col)
        used_dia2.add(row - col)
        queen1(used_cols, used_dia1, used_dia2)
        used_cols.remove(col)
        used_dia1.remove(row + col)
        used_dia2.remove(row - col)


queen1(set([0]), set([0]), set([0]))
print(c1[0])
