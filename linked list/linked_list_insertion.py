class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_between(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.insert_at_end(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.insert_at_begin(7); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.insert_at_begin(1); 
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.insert_at_end(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insert_at_between(llist.head.next, 8) 
  
    print('Created linked list is:') 
    llist.print_list() 
    
