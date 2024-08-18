class singlyLinkedList:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    
Head = singlyLinkedList(1)
A = singlyLinkedList(3)
B = singlyLinkedList(5)
C = singlyLinkedList(7)

Head.next = A
A.next = B
B.next = C


def printLL(Head):
    curr = Head
    ele = []
    

    while curr:
        ele.append(str(curr.val))
        
        curr = curr.next
    
    print(" -> ".join(ele))

printLL(Head)