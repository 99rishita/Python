def isSumProperty(root):
    '''
    :param root: root of the given tree.
    :return: 1 or 0 , as per the above statement
    {
        # Node Class:
        class Node:
            def init(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    # code here
    if root is None or (root.left is None and root.right is None):
        return 1
    if root:
        lchild = 0
        rchild = 0
        temp = root
        if temp.left is not None:
            lchild = temp.left.data
        else:
            lchild = 0
        if temp.right is not None:
            rchild = temp.right.data
        else:
            rchild = 0
        if (temp.data == lchild+rchild) and isSumProperty(temp.left) and isSumProperty(temp.right):
            return 1
        else:
            return 0