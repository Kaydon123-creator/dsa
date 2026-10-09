# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def dfs(root):
            if not root:
                return 0
            l = root.left 
            r = root.right 
            i = j = 1 
            while l:
                i+=1
                l = l.left
            while r:
                j+=1
                r = r.right 
            if i == j:
                print(2**i - 1, root.val)
                return 2**i - 1 
            return 1 + dfs(root.left) + dfs(root.right)
        return dfs(root)
       
        