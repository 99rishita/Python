len_list = mid_ele = 0
    ind = 0
    c = -1
    temp = head
    while(temp):
        len_list += 1
        temp = temp.next
    if len_list%2 == 0:
        ind = int(len_list/2)
    else:
        ind = int(len_list/2)
    t = head
    while(t):
        c += 1
        if ind == c:
            return t
        t = t.next

#########################################################################################################


def findMid(head):
    # Code here
    first_temp = head
    second_temp = head
    if head != None:
        while(second_temp != None and second_temp.next != None):
            second_temp = second_temp.next.next
            first_temp = first_temp.next
        
        return first_temp