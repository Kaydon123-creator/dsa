# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 
        def dfs(node, max):
            nonlocal res 
            if not node:
                return 
            if node.val >= max:
                res+=1 
                max = node.val 
            dfs(node.left, max)
            dfs(node.right, max)
        dfs(root, root.val)
        return res

            


        