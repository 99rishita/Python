def buildtreeutil(In, post, instrt, inend, pindex):
    if instrt > inend:
        return None
    
    node = Node(post[pindex[0]])
    pindex[0] -= 1
    
    if instrt == inend:
        return node
    
    iindex = search(In, instrt, inend, node.data)
    
    node.right = buildtreeutil(In, post, iindex+1, inend, pindex)
    node.left = buildtreeutil(In, post, instrt, iindex-1, pindex)
    
    return node
    
def buildTree(In, post, n):
    
    # your code here
    pindex = [n-1]
    return buildtreeutil(In, post, 0, n-1, pindex)
    
def search(In, instrt, inend, value):
    for i in range(instrt, inend+1):
        if In[i] == value:
            break
    return i 