# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(root, curr):
            if not root:
                return 
            curr.append(root.val)
            if not root.left and not root.right:
                if sum(curr)==targetSum:
                    result.append(curr[:])
                else:
                    pass
            dfs(root.right, curr)
            dfs(root.left, curr)
            curr.pop()
        dfs(root, [])
        return result
        