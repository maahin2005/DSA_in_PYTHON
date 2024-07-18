class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

arr = [2,5,7,3,4]

def convertIntoLL(arr):
    if not arr:
        return None
    head =  Node(arr[0])
    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

head = convertIntoLL(arr)

temp = head

while(temp):
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
