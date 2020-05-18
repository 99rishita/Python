def skipMdeleteN(head, M, N):
    # Code here
    current = head
    while(current):
        for i in range(1, M):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        t = current.next
        for i in range(1, N+1):
            if t is None:
                break
            t = t.next
        current.next = t
        current = t