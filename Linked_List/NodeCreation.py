class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


x = Node(1)
y = Node(2)
x.next = y


new_node = Node(3)
new_node.next = x

head_node = Node(5)
head_node.next = new_node
print(head_node.next.data)

