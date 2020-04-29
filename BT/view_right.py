def rightviewutil(root, level, max_level):
    if root is None:
        return
    if max_level[0] < level:
        print(root.data,end=" ")
        max_level[0] = level
        
    rightviewutil(root.right, level+1, max_level)
    rightviewutil(root.left, level+1, max_level)
    
    
def rightView(root):
    '''
    :param root: root of given tree.
    :return: print the right view of tree, dont print new line
    '''
    # code here
    max_level = [0]
    rightviewutil(root, 1, max_level)