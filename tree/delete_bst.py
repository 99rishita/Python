class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, key):
    if root is None:
        root = Node(key)
    if root:
        if key<root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                insert(root.left, key)
        elif key>root.data:
            if root.right is None:
                root.right = Node(key)
            else:
                insert(root.right, key)

def minvalue(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if root:
        if key<root.data:
            root.left = delete(root.left, key)
        elif key>root.data:
            root.right = delete(root.right, key)
        else:
            if root.left != None and root.right != None:    
                temp = minvalue(root.right)
                root.data = temp.data
                root.right = delete(root.right, temp.data)
            elif root.left is None:
                root = root.right
                #root = None
                #return temp
            elif root.right is None:
                root = root.left
                #root = None
                #return temp
            else:
                root = None
        return root

def inorder_print(root):
    if root:
        inorder_print(root.left)
        print(root.data)
        inorder_print(root.right)

root=Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 10)
print('before deletion')
inorder_print(root)
delete(root, 60)
print('after deletion')
inorder_print(root)


