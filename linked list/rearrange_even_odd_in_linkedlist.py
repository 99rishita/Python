#User function Template for python3

def rearrangeEvenOdd(head):
    #code here
    odd_node = head
    even_node = head.next
    evenfirst = even_node
    while(1==1):
        if odd_node == None or even_node == None or even_node.next == None:
            odd_node.next = evenfirst
            break
        
        odd_node.next = even_node.next
        odd_node = even_node.next
        
        if odd_node.next == None:
            even_node.next = None
            odd_node.next = evenfirst
            break
        
        even_node.next = odd_node.next
        even_node = odd_node.next
        
    return head