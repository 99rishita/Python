class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, key):
    if root is None:
        root = node(key)
    if root:
        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                insert(root.right, key)

'''def min(root, lcount):
    current = root
    while(current.left is not None):
        current = current.left
        lcount += 1
    return lcount

def max(root, rcount):
    current = root
    while(current.right is not None):
        current = current.right
        rcount += 1
    return rcount

def height(root):
    if root is None:
        return 0
    if root:
        if min(root, lcount) > max(root, rcount):
            return min(root, lcount) + 1
        else:
            return max(root, lcount) + 1 '''
def height(root):
    if root is None:
        return 0
    if root:
        ldepth = height(root.left)
        rdepth = height(root.right)
        
        if ldepth<rdepth:
            return rdepth+1
        else:
            return ldepth+1


'''root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.right = Node(0)
root.left.left.left = Node(6)'''
root = Node(20)
insert(root, 8) 
insert(root, 22) 
insert(root, 4) 
insert(root, 12) 
insert(root, 10)   
insert(root, 14)    
#lcount = 0
#rcount = 0
#min(root, lcount)
#max(root, rcount)
print(height(root))