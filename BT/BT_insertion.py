class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def level_order_insert(root, key):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right) 

root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7)  
root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)  
  
print("Inorder traversal before insertion:", end = " ") 
inorder(root)  
  
key = 12
level_order_insert(root, key) 

  
print()  
print("Inorder traversal after insertion:", end = " ") 
inorder(root) 