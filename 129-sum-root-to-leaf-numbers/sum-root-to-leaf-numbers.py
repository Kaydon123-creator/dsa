# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        result = []

        def dfs(root, curr):
            if not root:
                return 
            curr+= str(root.val) 
            if not(root.left or root.right):
                result.append(curr)
            if root.left:
                dfs(root.left, curr)
            if root.right:
                dfs(root.right, curr)
        dfs(root, "")
  
        return sum([int(x) for x in result])

        