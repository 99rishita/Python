class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def search(root, key):
    if root is None:
        print("no such element")
    elif root==key:
        return root
    elif key>root.data:
        search(root.right, key)
    elif key<root.data:
        search(root.left, key)

def insert(root, value):
    if root is None:
        root = Node(value)
    elif value<root.data:
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)

def inorder_print(root):
    if root:
        inorder_print(root.left)
        print(root.data)
        inorder_print(root.right) 

def preorder_print(root):
    if root:
        print(root.data)
        preorder_print(root.left)
        preorder_print(root.right)

def postorder_print(root):
    if root:
        postorder_print(root.left)
        postorder_print(root.right)
        print(root.data)
    
def levelorder_print(root):
    if root is None:
        return root
    q = []
    q.append(root)
    while(len(q)>0):
        temp = q.pop(0)
        print(temp.data)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)



root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 60)
#inorder_print(root)
#preorder_print(root)
#postorder_print(root)
#levelorder_print(root)
print(search(root,2))

    