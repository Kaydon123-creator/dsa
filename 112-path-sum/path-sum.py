# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = targetSum
        def dfs(root, sum):
            if not root:
                return False
            sum -= root.val
            if sum == 0 and not(root.left or root.right):
                return True
            else:
                return dfs(root.left, sum) or dfs(root.right, sum)
        return dfs(root, sum)
        