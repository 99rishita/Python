class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
        self.h = 0

def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1

def distnodeutil(root, d):
    lis = []
    if root is None or d < 0:
        return

    if d == 0:
        lis.append(root.data)
        print(lis)
    distnodeutil(root.left, d-1)
    distnodeutil(root.right, d-1)

def dist_node(root, dest, d):
    lis = []
    if root is None:
        return root
    if dest.data == root.data:
        h = height(root)
        print(h)
        distnodeutil(root, d)

    dist_node(root.left, dest, d)
    dist_node(root.right, dest, d)

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

(dist_node(root, Node(5), 2))
actual_h = (height(root))
