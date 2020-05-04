class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def consutil(ino, pre, instrt, inend, pindex):
    if instrt > inend:
        return None
    
    node = Node(pre[pindex[0]])
    pindex[0] += 1

    if instrt == inend:
        return node

    iindex = search(ino, instrt, inend, node.data)

    node.left = consutil(ino, pre, instrt, iindex-1, pindex)
    node.right = consutil(ino, pre, iindex+1, inend, pindex)

    return node

def search(ino, instrt, inend, value):
    for i in range(instrt, inend+1):
        if ino[i] == value:
            break
    return i


def cons(ino, pre):
    pindex = [0]
    n = len(ino)
    return consutil(ino, pre, 0, n-1, pindex)

def postOrder(node): 
    if node == None:  
        return
    postOrder(node.left)  
    postOrder(node.right) 
    print(node.data,end=" ") 

def inorder(node): 
    if node == None:  
        return
    inorder(node.left)
    print(node.data,end=" ")   
    inorder(node.right) 
    
  
# Driver code  
if __name__ == '__main__': 
    '''ino = [9,3,15,20,7] 
    pre = [3,9,20,15,7]'''
    ino = ['D', 'B', 'E', 'A', 'F', 'C'] 
    pre = ['A', 'B', 'D', 'E', 'C', 'F']   
    #n = len(In) 
  
    root = cons(ino, pre)  
  
    print("inorder of the constructed tree :")  
    #postOrder(root)
    inorder(root) 