class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    
    def listlength(self):
        tempNode = self.head
        count = 0
        while tempNode is not None:
            count += 1
            tempNode = tempNode.next
        return count

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertbegin(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode 
        del tempNode

    def insertbetween(self, newNode, pos):
        if(pos==0):
            self.insertbegin(newNode)
            return
        if(pos<0 or pos>self.listlength()):
            print("Invalid")
            return
        tempNode = self.head
        temppos = 0
        while True:
            if(temppos == pos):
                previousNode.next = newNode
                newNode.next = tempNode
                break
            previousNode = tempNode
            tempNode = tempNode.next
            temppos += 1

    def delHead(self):
        if self.isEmpty() is False:
            temp = self.head
            self.head = self.head.next
            temp = None
        else:
            print("no delete")

    def delend(self):
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None

    def delBetween(self, pos):
        currentpos = 0
        temp = self.head
        while True:
            if(currentpos == pos):
                prev.next = temp.next
                temp.next = None
                break
            prev = temp
            temp = temp.next
            currentpos += 1

        

    def print(self):
        tempNode = self.head
        while True:
            if tempNode is None:
                break
            print(tempNode.data)
            tempNode = tempNode.next

firstNode = Node("john")
linkedlist = Linkedlist()
linkedlist.insertEnd(firstNode)
secondNode = Node("perry")
linkedlist.insertEnd(secondNode)
thirdNode = Node("chris")
linkedlist.insertbegin(thirdNode)
fourthNode = Node("david beckam")
linkedlist.insertbegin(fourthNode)
fifthNode = Node("harry")
linkedlist.insertbetween(fifthNode,2)
sixthNode = Node("george")
linkedlist.insertbetween(sixthNode, 0)
#linkedlist.delend()
#linkedlist.delBetween(2)
#linkedlist.delHead()
linkedlist.print()
