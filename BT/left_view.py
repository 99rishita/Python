class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def leftview(root):
    if root is None:
        return
    q = []
    q.append(root)
    q.append(None)
    while(len(q)):
        temp = q[0]
        if (temp):
            print(temp.data)
            while(q[0]!= None):
                temp = q[0]
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                q.pop(0)
            q.append(None)
        q.pop(0)



'''root = Node(4)  
root.left = Node(5)    
root.right = Node(2)  
root.right.left = Node(3)  
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(6)
root.left.right.right.right = Node(9) '''
root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)


(leftview(root))