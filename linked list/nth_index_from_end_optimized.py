def getNthfromEnd(head,n):
    #code here
    current = head
    prev = head
    while(n):
        if current == None:
            return -1
        current = current.next
        n -= 1
    while(current!=None):
        current = current.next
        prev = prev.next
    return prev.data