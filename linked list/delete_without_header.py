#User function Template for python3
'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def deleteNode(curr_node):
    #code here
    temp = 0
    temp = curr_node.data
    curr_node.data = curr_node.next.data
    curr_node.next.data = temp
    curr_node.next = curr_node.next.next
        
###################################################################################################################3

def deleteNode(curr_node):
    #code here
    temp = 0
    temp = curr_node.next
    curr_node.data = temp.data
    curr_node.next = temp.next
    temp = None