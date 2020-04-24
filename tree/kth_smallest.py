class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def insert(root, key):
    if root is None:
        root = node(key)
    if root:
        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                insert(root.right, key)

def inorder(root, stack):
    if root:
        inorder(root.left, stack)
        stack.append(root.data)
        inorder(root.right, stack)

def kth_smallest(stack, k):
    for i in range(len(stack)):
        if i == k:
            kth_smallest.small= stack[i-1]

root = Node(50) 
insert(root, 30) 
insert(root, 20) 
insert(root, 40) 
insert(root, 70) 
insert(root, 60) 
insert(root, 80)
stack = []
inorder(root, stack)
kth_smallest.small = None
kth_smallest(stack, 3)

if kth_smallest.small is not None:
    print(kth_smallest.small)