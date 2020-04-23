class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def succ_pred(root, key):
    if root:
        if key<root.data:
            succ_pred.succ = root
            return succ_pred(root.left, key)
        elif key>root.data:
            succ_pred.pred = root
            return succ_pred(root.right, key)
        else:
            if root.left:
                temp = root.left
                while(root.right is not None):
                    temp = temp.right
                    succ_pred.pred = temp

            if root.right:
                temp=root.right
                while(temp.left is not None):
                    temp = temp.left
                    succ_pred.succ = temp
            return


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

def inorder(root, stack):
    if root:
        inorder(root.left, stack)
        stack.append(root.data)
        inorder(root.right, stack)

'''def pred_succ(stack, key):
    j=0
    for i in range(len(stack)):
        if stack[i] == key:
            pred = stack[i-1]
            print(pred)
            succ = stack[i+1]
            print(succ) '''

root = Node(50) 
insert(root, 30); 
insert(root, 20); 
insert(root, 40); 
insert(root, 70); 
insert(root, 60); 
insert(root, 80); 
#stack = []
#inorder(root, stack)
#pred_succ(stack, 9)

succ_pred.pred = None
succ_pred.succ = None
  
succ_pred(root, 60) 
  
if succ_pred.pred is not None: 
    print("Predecessor is", succ_pred.pred.data) 
  
else: 
    print("No Predecessor")
  
if succ_pred.succ is not None: 
    print("Successor is", succ_pred.succ.data) 
else: 
    print("No Successor")
