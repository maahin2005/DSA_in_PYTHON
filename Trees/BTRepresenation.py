class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(5)
root.left = Node(3)
root.right = Node(4)

print(root.data)
print(root.left.data)
print(root.right.data)