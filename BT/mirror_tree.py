class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function
def mirror(root):
    # Code here
    if root:
        temp = root
        mirror(root.left)
        mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp