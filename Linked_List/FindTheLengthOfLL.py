class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def convertToLL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

arr = [2,4,6,8,10,1,2,4]
head = convertToLL(arr)

cnt = 0

def findLengthOfLL(head):
    temp = head
    while(temp):
        temp = temp.next
        global cnt
        cnt+=1
    return cnt

print("Length: ",findLengthOfLL(head))
    




