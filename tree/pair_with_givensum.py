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

def isPairPresent(root,summ): 
    if root:
        if summ < root.data:
            return isPairPresent(root.left, summ)
            summ = summ - root.data
            return summ
        if summ == root.data:
            print('no sum is present')
        if summ > root.data:
            return isPairPresent(root.right, summ)
            summ = summ - root.data
            return summ

def search(root, key):
    if root:
        if key < root.data:
            return search(root.left, key)
        if key == root.data:
            return 1
        if key > root.data:
            return search(root.right, key)
        return 0


root = Node(15)
insert(root, 10) 
insert(root, 20) 
insert(root, 8) 
insert(root, 12) 
insert(root, 16) 
insert(root, 25)
sum = 0
sum = isPairPresent(root, 33)
print(sum)
print(search(root, sum))
