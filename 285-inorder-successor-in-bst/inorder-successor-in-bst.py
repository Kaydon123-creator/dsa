# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        successor = False
        res = None
        def dfs(node):
            nonlocal res, successor
            if not node :
                return node

            dfs(node.left)

            if node.val == p.val :
                successor = True 

            if successor and node.val != p.val:
                successor = False
                res = node

            dfs(node.right) 
            
            
        dfs(root)
        return res
            

            
            




        