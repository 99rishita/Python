from collections import deque
class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
s = Stack()

def larger(arr):
    s.push(arr[0])
    for i in range(1,len(arr)):
        next=arr[i]
        if(s.isEmpty()==False):
            x=s.pop()
            while(next>x):
                print(next)
                if(s.isEmpty()==True):
                    break
                x=s.pop()
            if(x>next):
                s.push(x)
        s.push(next)
    while(s.isEmpty()==False):
        x = s.pop()
        next=-1
        print(next)
arr=[4,3,2,1]
larger(arr)
            
            

