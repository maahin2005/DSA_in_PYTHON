class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def converToLL(arr):
    head = Node(arr[0])

    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

arr = [1,3,5,7,9]
head = converToLL(arr)

def findTheElInLL(head, el):

    temp = head

    while(temp):
        if temp.data == el:
            return 1
        temp = temp.next

    return 0

ans = findTheElInLL(head, 31)
print(ans)
    
