class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        
def printlist():
    global head
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next

def push(key):
    global head
    new_node = Node(key)
    new_node.next = head
    head = new_node
    return head
    
def segregate():
    global head
    even_start = None
    even_end = None
    odd_start = None
    odd_end = None
    current_node = head
    while(current_node):
        val = current_node.data
        if val%2==0:
            if even_start == None:
                even_start = current_node
                even_end = even_start
            else:
                even_end.next = current_node
                even_end = even_end.next
        else:
            if odd_start == None:
                odd_start = current_node
                odd_end = odd_start
            else:
                odd_end.next = current_node
                odd_end = odd_end.next
        current_node = current_node.next
    if odd_start == None or even_start == None:
        return
    even_end.next = odd_start
    odd_end.next = None
    head = even_start
        
        
head = None
'''push(11) 
push(10) 
push(9) 
push(6) 
push(4) 
push(1) 
push(0) '''
push(10) 
push(9) 
push(8) 
push(7) 
push(6) 
push(5) 
push(4) 
push(3) 
push(2) 
push(1) 

print( "Given linked list: ", end = "") 
printlist() 
          
segregate() 
      
print("\nAfter rearrangement: ", end = "") 
printlist() 