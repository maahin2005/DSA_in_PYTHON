class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self,root):
        result = []
        self.__helper__(root,result)
        return result
    
    def __helper__(self,root,result):
        if not root:
            return
        
        self.__helper__(root.left,result)
        self.__helper__(root.right,result)
        result.append(root.val)

root = Node(12)
root.left = Node(9)
root.right = Node(15)
root.left.left = Node(5)
root.left.right= Node(11)
root.right.left = Node(14)
root.right.right = Node(18)
root.left.left.left = Node(2)
root.left.left.right = Node(7)

sol = Solution()
ans = sol.postorderTraversal(root)
print(ans)

