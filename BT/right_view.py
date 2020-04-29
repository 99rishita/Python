class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def rightview(root):
    if root is None:
        return root
    q = []
    q.append(root)
    q.append(None)
    while(len(q)):
        temp = q[0]
        if (temp):
            while(q[0]!= None):
                temp = q[0]
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                remp = q.pop(0)
            print(remp.data)
            q.append(None)
        q.pop(0)

'''root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7) '''

'''root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(15)
root.right.right.left = Node(14) '''

root = Node(58)
root.left = Node(31)
root.right = Node(68)
root.left.left = Node(9)
root.left.right = Node(56)
root.right.left = Node(63)
root.left.left.left = Node(5)
root.left.left.right = Node(10)
root.left.right.left = Node(42)
root.left.right.right = Node(57)
root.right.left.left = Node(61)
root.right.left.right = Node(67)
root.left.left.left.right = Node(3)



(rightview(root))