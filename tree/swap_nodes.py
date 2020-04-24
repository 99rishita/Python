class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.temp = 0 
        
def swap_node(root):
    if root:
        swap_node(root.left)
        if prev!=None and root.data<prev.data:
            if first is None:
                first = prev
                middle = root
            else:
                last = root
        prev = root
        swap_node(root.right)

def swap(root):
    swap_node(root)
    if first != None and middle != None:
        root.temp = first.data
        first.data = middle.data
        middle.data = root.temp
    
    elif first != None and last != None:
        root.temp = first.data
        first.data = last.data
        last.data = root.temp

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(6) 
root.left = Node(10) 
root.right = Node(2) 
root.left.left = Node(1) 
root.left.right = Node(3) 
root.right.right = Node(12) 
root.right.left = Node(7)
print('inorder traversal before swapping')
inorder(root)
#swap_node(root)
swap(root)
print('inorder traversal after swapping')
inorder(root)

    


            


        