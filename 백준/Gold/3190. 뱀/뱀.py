import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

apples = []
for _ in range(k):
    apples.append(tuple(map(int, sys.stdin.readline().split())))

l = int(sys.stdin.readline())
rotates = deque()

for _ in range(l):
    rotates.append(tuple(sys.stdin.readline().split()))

dir_pos = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
dirs = ["R", "D", "L", "U"]
cur_dir = 0

time = 0
snakes = deque([(1, 1)])


def get_next_pos(cur, d_idx):
    cy, cx = cur
    dy, dx = dir_pos[dirs[d_idx]]

    return (cy + dy, cx + dx)


def is_crash(next):
    ny, nx = next
    is_wall = ny > n or nx > n or nx <= 0 or ny <= 0
    is_snake = any(ny == sy and nx == sx for sy, sx in list(snakes)[:-1])

    return is_wall or is_snake


while True:
    time += 1
    ny, nx = get_next_pos(snakes[-1], cur_dir)

    # 사과처리
    is_apple = any(ny == ay and nx == ax for ay, ax in apples)
    if is_apple:
        apples.remove((ny, nx))

    # 충돌 확인
    if is_crash((ny, nx)):
        break

    # move
    if not is_apple:
        snakes.popleft()
    snakes.append((ny, nx))

    # 방향전환
    rt, rd = rotates[0] if rotates else (-1, -1)
    if time == int(rt):
        cur_dir = (cur_dir + (1 if rd == "D" else -1)) % 4
        rotates.popleft()

print(time)
