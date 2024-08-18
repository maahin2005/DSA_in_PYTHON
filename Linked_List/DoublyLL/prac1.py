class doublyNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

head = tail = doublyNode(1)

def display(head):
    curr = head
    ele = []

    while curr:
        ele.append(str(curr.val))
        curr = curr.next
    
    print(" <-> ".join(ele))

def insert_at_begining(head,tail,val):
    new_node = doublyNode(val,next=head)
    head.prev = new_node

    return new_node,tail

def insert_at_ending(head,tail,val):
    new_node = doublyNode(val,prev=tail)
    tail.next = new_node

    return head,new_node

def delete_at_beginning(head,tail):
    
    new_node = head.next
    head.next.prev = new_node

    return new_node,tail

def delete_at_ending(head,tail):
    new_tail = tail.prev
    new_tail.next = None
    return head,tail

def delete_any_val(head,tail,val):

    curr = head
    
    if val == head.val:
        return delete_at_beginning(head,tail)
    if val == tail.val:
        return delete_at_ending(head,tail)

    while curr:
        if val == curr.val:
            left = curr.prev
            right = curr.next
            left.next = right
            right.prev = left
        curr = curr.next
    return head , tail

head,tail = insert_at_begining(head,tail,0)
head,tail = insert_at_ending(head,tail,3)
head,tail = insert_at_ending(head,tail,5)
head,tail = insert_at_ending(head,tail,7)
head,tail = insert_at_ending(head,tail,11)
head,tail = delete_at_beginning(head,tail)
head,tail = delete_any_val(head,tail,11)
head,tail = delete_at_ending(head,tail)
display(head)
