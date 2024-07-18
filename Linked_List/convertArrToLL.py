class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def convertArrToLL(arr):
    if not arr:
        return None
     
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
       temp = Node(arr[i])
       mover.next = temp   # Link the current node to the new node
       mover = temp
    
    return head

print(convertArrToLL([1,2,3,4,5]).data)