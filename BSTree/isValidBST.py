class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left    
        self.right = right

class Solution:
    def isBST(self,root):
        return self.__helper__(root,float('-inf'),float('inf'))
         
    
    def __helper__(self, root, minValue, maxValue):
        if not root: return True

        if root.val >= maxValue or root.val <= minValue: return False

        return self.__helper__(root.left,minValue,root.val) and self.__helper__(root.right,root.val,maxValue)


root = Node(9)
root.left = Node(7)
root.right = Node(11)
root.left.left = Node(5)
root.left.right = Node(8)
root.right.left = Node(10)
root.right.right = Node(13)

sol = Solution()
ans = sol.isBST(root)
print(ans)