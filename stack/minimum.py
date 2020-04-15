class Stack:
    def __init__(self):
        self.minEle = 0
        self.stack = []
    
    def isEmpty(self):
        if(self.stack == []):
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]
    
    def push(self, x):
        if(self.isEmpty()==True):
            self.stack.append(x)
            self.minEle = x
        elif(x>self.minEle):
            self.stack.append(x)
        else:
            self.stack.append(2*x - self.minEle)
            self.minEle = x

    def pop(self):
        if(self.peek()>self.minEle):
            return self.stack.pop()
        else:
            self.minEle = 2*self.minEle - self.peek()
            self.stack.pop()

    def min(self):
        return self.minEle

s = Stack()
s.push(8)
s.push(10)
s.push(6)
s.push(3)
s.push(7)
print(s.pop())
#print(s.peek())
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
