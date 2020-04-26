class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def deepest_node(root):
    if root is None:
        return 0

    ldepth = deepest_node(root.left)
    rdepth = deepest_node(root.right)

    return max(ldepth, rdepth) + 1

def deep_node(root, levels):
    if not root:
        return
    if levels == 1:
        return root.data
    elif (levels > 1):
        deep_node(root.left, levels-1)
        deep_node(root.right, levels-1)

def delete(root, key):
    if root is None:
        return None
    if root:
        q = []
        q.append(root)
        while(len(q)):
            temp = q.pop(0)
            if temp.left is not None and temp.data != key:
                q.append(temp.left)
            if temp.right is not None and temp.data != key:
                q.append(temp.right)
            if temp.data == key:
                x = deep_node(root, levels)
                print(x)
                temp.data = x
                

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

print("Inorder traversal before deletion:", end = " ") 
inorder(root)  

levels = deepest_node(root)
deep_node(root, levels)
delete(root, 7)

print("Inorder traversal after deletion:", end = " ") 
inorder(root)  


            
