class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self,root):
        result = []
        self.__helper__(root,result)
        return result
    
    def __helper__(self,root,result):
        if not root:
            return
        
        self.__helper__(root.left,result)
        result.append(root.val)
        self.__helper__(root.right,result)


root = Node(11)
root.left = Node(5)
root.right = Node(13)
root.left.left = Node(3)
root.left.right = Node(8)
root.left.right.left = Node(6)
root.left.right.right = Node(9)
root.right.left = Node(12)
root.right.right = Node(17)
root.right.right.left = Node(14)
root.right.right.right = Node(16)

sol = Solution()

ans = sol.inorderTraversal(root)

print(ans)