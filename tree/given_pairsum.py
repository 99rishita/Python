class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, key):
    if root is None:
        root = Node(key)
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

def given_sum(stack, sum):
    s = set()
    for i in range(len(stack)):
        temp = sum - stack[i]
        if temp in s:
            return 1
        s.add(stack)
    return 0


root = Node(15)
insert(root, 10) 
insert(root, 20) 
insert(root, 8) 
insert(root, 12) 
insert(root, 16) 
insert(root, 25)
stack = []
sum = 20
inorder(root, stack)
print(stack)
print(given_sum(stack, sum))



