# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        prev = None
        
        def dfs(root):
            nonlocal result
            nonlocal prev
            if not root:
                return 
            
            dfs(root.left)
            if prev is not None:
                result = min(abs(root.val - prev), result)
            prev = root.val
            dfs(root.right)
            

        dfs(root)
        return result
        