class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, key):  
  
    if (not root): 
        return Node(key)  
    if (key < root.data):  
        root.left = insert(root.left, key)  
    else: 
        root.right = insert(root.right, key)  
    return root  

def floor_node(root, key):
    if root is None:
        return root
    
    if key < root.data:
        return floor_node(root.left, key)

    if key == root.data:
        return root.data

    floorValue = floor_node(root.right, key)
    return floorValue if (floorValue <= key) or (floorValue is None) else root.data

if __name__ == '__main__': 

    root = Node(8)   
    root.left = Node(4) 
    root.right = Node(12) 
    root.left.left = Node(2) 
    root.left.right = Node(6) 
    root.right.left = Node(10) 
    root.right.right = Node(14) 
    print(floor_node(root, 13)) 
