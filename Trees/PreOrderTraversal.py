class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self,root):
        result = []
        self._helper_(root,result)
        return result
    
    def _helper_(self,root,result):
        if not root: return

        result.append(root.val)
        self._helper_(root.left,result)
        self._helper_(root.right,result)


root = Node(7)
root.left = Node(5)
root.right = Node(10)
root.left.left = Node(2)
root.right.left = Node(9)
root.left.right = Node(6)
root.right.right = Node(12)

sol = Solution()
ans = sol.preorderTraversal(root)
print(ans)
