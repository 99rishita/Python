class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def lca(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left_lca = lca(root.left, n1, n2)
    right_lca = lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(9)
root.left.right.left = Node(10)

print(lca(root, 4, 10).data)