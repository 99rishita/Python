# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    # Code here
    count = 1
    temp = head
    while(temp):
        if k == 1:
            head = temp.next
            temp.next = None
        if count == k-1:
            temp.next = temp.next.next
        temp = temp.next
        count += 1
    return head