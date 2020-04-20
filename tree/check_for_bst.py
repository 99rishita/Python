class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root, stack):
    if root:
        inorder(root.left, stack)
        stack.append(root.data)
        inorder(root.right, stack)

def isbstvalid(root):
    for i in range(0, len(stack)):
        if(stack[i]>stack[i+1]):
            return False
        else:
            return True


stack = []
root = Node(3)
root.left = Node(2)
root. right = Node(5)
inorder(root, stack)

if(isbstvalid(root)):
    print('bst')
else:
    print('not bst')

