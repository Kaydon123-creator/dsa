class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root

        def flatten(node):
            if not node:
                return node
            
            r = flatten(node.right) if node.right else None

            l = flatten(node.left)

            node.right = l 

            node.left = None 

            par = node
            
            while node.right:
                node = node.right
           
            node.right = r 

            return par

        return flatten(root)
            


            
        


     
