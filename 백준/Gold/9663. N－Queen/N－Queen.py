n = int(input())

c = [0]


def search(path, used_cols, used_diag1, used_diag2):
    y = len(path)  # 현재 행(row) 번호
    # base case
    if y == n:
        # print(path)
        c[0] += 1
        return

    # 현재 row에서 올바른 열번호 찾기
    for x in range(n):
        if x in used_cols or (y - x) in used_diag1 or (y + x) in used_diag2:
            continue
        # if any(x == px or abs(py - y) == abs(px - x) for py, px in path):
        #     continue

        used_cols.add(x)
        used_diag1.add((y - x))
        used_diag2.add((y + x))
        path.append((y, x))

        search(path, used_cols, used_diag1, used_diag2)

        used_cols.remove(x)
        used_diag1.remove((y - x))
        used_diag2.remove((y + x))
        path.pop()


search([], set(), set(), set())
print(c[0])
