class Heap:
    def __init__(self):
        self.list = []

    def push(self, v):
        self.list.append(v)
        self._heaplify_up()

    def pop(self):
        if not self.list:
            return None
        root = self.list[0]
        if len(self.list) > 0:
            self.list[0] = self.list[-1]
            self.list.pop()
            self._heaplify_down()
        return root

    # 루트에서 위치찾기
    def _heaplify_down(self):
        cur = 0
        size = len(self.list)

        while True:
            left = cur * 2 + 1
            right = cur * 2 + 2
            largest = cur

            if left < size and self.list[left] > self.list[largest]:
                largest = left
            if right < size and self.list[right] > self.list[largest]:
                largest = right

            if largest == cur:
                break

            self.list[cur], self.list[largest] = self.list[largest], self.list[cur]
            cur = largest

    # 힙 끝단 값에서 위치찾기
    def _heaplify_up(self):
        cur = len(self.list) - 1
        while cur > 0:
            parent = (cur - 1) // 2
            if self.list[cur] > self.list[parent]:
                self.list[parent], self.list[cur] = self.list[cur], self.list[parent]
                cur = parent
            else:
                break

    def __bool__(self):
        return len(self.list) > 0

    def __str__(self):
        return str(self.list)


import sys

n = int(sys.stdin.readline())
commands = list(map(int, sys.stdin.readlines()))
h = Heap()

for com in commands:
    if com == 0:
        print(h.pop() if h else 0)
    else:
        h.push(com)
