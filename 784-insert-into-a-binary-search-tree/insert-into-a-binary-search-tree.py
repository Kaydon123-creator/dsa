# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def insert(root):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = insert(root.right)
                
            elif val < root.val:
                root.left = insert(root.left)
            
            return root 
        return insert(root)



            
            


        