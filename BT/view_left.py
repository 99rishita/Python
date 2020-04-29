def leftviewutil(root, level, max_level):
    if root is None:
        return
    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level
    leftviewutil(root.left, level+1, max_level)
    leftviewutil(root.right, level+1, max_level)
    
def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    max_level = [0]
    leftviewutil(root, 1, max_level)
