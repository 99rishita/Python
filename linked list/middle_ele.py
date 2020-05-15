class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
            print(temp.data, end=" ")
            temp = temp.next

    def getCount(self):
    #code here
        count = -1
        temp = self.head
        while(temp):
            count += 1
            print('index is:', count)
            temp = temp.next
        print('\nlength of linked list is:', count)

    def findindex(self, ind):
        t = self.head
        c = -1
        while(t):
            c += 1
            if ind == c:
                print(t.data)
            t = t.next

    def findMid(self):
    # Code here
        len_list = 0
        ind = 0
        temp = self.head
        while(temp):
            len_list += 1
            temp = temp.next
        if len_list%2 == 0:
            ind = int(len_list/2)
        else:
            ind = int(len_list/2)
        llist.findindex(ind)
    
    

if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.insert_at_end(1) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.insert_at_end(2); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.insert_at_end(3); 
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.insert_at_end(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insert_at_end(5) 
    llist.insert_at_end(6) 
  
    print('Created linked list is:') 
    llist.print_list() 

    llist.getCount()
    print('middle element is:')
    llist.findMid()
  