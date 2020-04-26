class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def isbalanced(root):
    if root is None:
        return 0,True

    ldepth, is_lbalanced = isbalanced(root.left)
    rdepth, is_rbalanced = isbalanced(root.right)

    if not is_lbalanced:
        return False

    if not is_rbalanced:
        return False
    
    if abs(ldepth - rdepth) > 1:
        return False

    return max(ldepth, rdepth) + 1, True


root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7)  
root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)  

print(isbalanced(root))
