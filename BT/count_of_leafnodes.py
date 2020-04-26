'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root):
    # Code here
    if root is None:
        return 0
    if root:
        q = []
        count = 0
        q.append(root)
        while(len(q)):
            temp = q.pop(0)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
            if temp.left is None and temp.right is None:
                count += 1
        return count
                
