class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

Your task is to return the count of elements
in the given linked list

Function Arguments: head_node (head of the linked list)
Return Type: Integer

	Contributed By: Nagendra Jha
'''
def getCount(head_node):
    #code here
    count = 0
    temp = head_node
    while(temp):
        count += 1
        temp = temp.next
    return count