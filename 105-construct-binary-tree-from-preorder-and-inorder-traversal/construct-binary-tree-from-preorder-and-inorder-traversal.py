# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        if not preorder and not inorder:
            return None
        if len(preorder) == len(inorder) == 1:
            return TreeNode(preorder[0])

        #retireve the root
        node = preorder[0]
        
        idx = inorder.index(node)
        #compute inorder for left subtree 
        right_inorder = inorder[idx+1:]
        #compute inorder for right subtree 
        left_inorder = inorder[:idx]
        #compute preorder for left subtree 
        left_preorder = preorder[1:idx+1]
        #compute preorder for right subtree 
        right_preorder = preorder[idx+1:]
        root = TreeNode(node)
        root.left =self.buildTree(left_preorder,left_inorder ) 
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

       
        


        