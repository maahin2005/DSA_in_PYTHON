class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelorderTraversal(self,root):

        result = []
        
        if not root:
            return result
        
        queue = []
        queue.append(root)

        while queue:
            q_size = len(queue)
            current_level = []

            for _ in range(q_size):
                current_node = queue.pop(0)

                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)

            result.append(current_level)
        
        return result
    
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
ans = sol.levelorderTraversal(root)
print(" ".join(map(str,ans)))