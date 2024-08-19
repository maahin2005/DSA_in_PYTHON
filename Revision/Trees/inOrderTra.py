class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def __helper__(root,result):
    if not root:
        return
    __helper__(root.left,result)
    result.append(root.val)
    __helper__(root.right,result)

def inOrderTravel(root):
    result = []
    
    __helper__(root,result)
    
    return result


Head = Node(10)
Head.left = Node(5)
Head.right = Node(15)
Head.left.left = Node(3)
Head.left.right = Node(7)
Head.right.right = Node(20)
Head.right.left = Node(12)

print(inOrderTravel(Head))

# 10
# 5 | 15
# 3 - 7 | 12 - 20

# 3, 5, 7, 10, 12, 15, 20