
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, v):
        new_node = Node(v)
        if self.root is None:
            self.root = new_node
            return
        cur = self.root
        while cur:
            dir = 'left' if v < cur.key else 'right'
            next_node = getattr(cur, dir)
            if next_node:
                cur = next_node
            else:
                setattr(cur, dir, new_node)
                break
    def post_order(self, node):
        if not node:
            return
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node.key)
        
        
            

import sys
sys.setrecursionlimit(10**6)

bst = BST()
nums = list(map(int,sys.stdin.readlines()))
for num in nums:
    bst.insert(num)
bst.post_order(bst.root)