class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.lcount = 0
        self.count = 0
        

def insert(root, key):
    if root is None:
        root = node(key)
    if root:
        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                insert(root.left, key)
                root.lcount +=1
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                insert(root.right, key)

def kth_smallest(root, k):
    if root is None:
        return None
    if root:
        #print(root.lcount)
        root.count = root.lcount + 1
        if root.count == k:
            return root
        elif root.count > k:
            return kth_smallest(root.left, k)
        else:
            return kth_smallest(root.right, k-root.count)
    

root = Node(50) 
insert(root, 30) 
insert(root, 20) 
insert(root, 40) 
insert(root, 70) 
insert(root, 60) 
insert(root, 80)
print(kth_smallest(root, 3).data)

