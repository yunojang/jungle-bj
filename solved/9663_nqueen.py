n = int(input())

c = [0]


def search(used_cols, used_diag1, used_diag2):
    y = len(used_cols)  # 현재 행(row) 번호
    # base case
    if y == n:
        # print(path)
        c[0] += 1
        return

    # 현재 row에서 올바른 열번호 찾기
    for x in range(n):
        if x in used_cols or (y - x) in used_diag1 or (y + x) in used_diag2:
            continue

        used_cols.add(x)
        used_diag1.add((y - x))
        used_diag2.add((y + x))

        search(used_cols, used_diag1, used_diag2)

        used_cols.remove(x)
        used_diag1.remove((y - x))
        used_diag2.remove((y + x))


search(set(), set(), set())
print(c[0])


def search(row, used_cols, used_diag1, used_diag2):
    pass
