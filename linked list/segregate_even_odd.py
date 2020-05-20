import collections
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        
def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next

def push(head, key):
    new_node = Node(key)
    new_node.next = head
    head = new_node
    return head
    
def segregate(head):
    d = collections.deque([])
    temp = head
    while(temp):
        if temp.data%2==0:
            d.appendleft(temp.data)
        else:
            d.append(temp.data)
        temp = temp.next
    temp = head
    
    while(len(d)):
        temp.data = d[0]
        d.popleft()
        temp = temp.next
        
    
        
head = None
head = push(head, 10) 
head = push(head, 9) 
head = push(head, 8) 
head = push(head, 7) 
head = push(head, 6) 
head = push(head, 5) 
head = push(head, 4) 
head = push(head, 3) 
head = push(head, 2) 
head = push(head, 1) 
      
print( "Given linked list: ", end = "") 
printlist(head) 
          
segregate(head) 
      
print("\nAfter rearrangement: ", end = "") 
printlist(head) 