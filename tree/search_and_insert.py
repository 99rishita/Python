class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    
def search(root,key):
    if root is None:
        return root
    if root:
        if key < root.data:
             return search(root.left, key)
        elif key == root.data:
            return root
        elif key> root.data:
            return search(root.right, key)
        else:
            return None

    
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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(4)
insert(root,2)
insert(root,1)
insert(root,3)
insert(root,5)
insert(root,6)
insert(root,7)
inorder(root)
print(search(root, 5))
