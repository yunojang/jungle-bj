class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._n = 0

    def append_tail(self, v):
        new_node = Node(v)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        self._n += 1

    def pop_head(self):
        if self.head is None:
            return None

        poped = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        self._n -= 1
        return poped.value

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.value, end="->" if cur.next else "\n")
            cur = cur.next

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if len(self) <= index:
            raise IndexError()

        cur = self.head
        cnt = 0
        while cnt < index:
            cur = cur.next
            cnt += 1
        return cur.value


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def dequeue(self):
        return self.list.pop_head()

    def enqueue(self, v):
        self.list.append_tail(v)

    def front_peek(self):
        return self.list.head.value

    def back_peek(self):
        return self.list.tail.value

    def __len__(self):
        return len(self.list)

    def __bool__(self):
        return len(self) > 0

    def __getitem__(self, index):
        return self.list[index]


import sys

n = int(sys.stdin.readline())
opers = list(map(lambda l: tuple(l.split()), sys.stdin.readlines()))

q = Queue()

for oper in opers:
    if oper[0] == "push":
        q.enqueue(oper[1])
    if oper[0] == "pop":
        print(q.dequeue() if q else -1)
    if oper[0] == "size":
        print(len(q))
    if oper[0] == "empty":
        print(0 if q else 1)
    if oper[0] == "front":
        print(q.front_peek() if q else -1)
    if oper[0] == "back":
        print(q.back_peek() if q else -1)
