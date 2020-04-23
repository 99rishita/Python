class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def LCA(root,n1,n2):
    if root is None:
        return root
    if root:
        if(root.data > n1 and root.data > n2): 
            return LCA(root.left, n1, n2) 
    
        if(root.data < n1 and root.data < n2): 
            return LCA(root.right, n1, n2) 
  
    return root 

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
print(LCA(root, 14, 8).data)