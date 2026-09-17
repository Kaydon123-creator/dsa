# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = root.val
        stack = [(root, False)]  # (node, visited)
        path_sum = {}  # stores best downward path for each node
        
        while stack:
            node, visited = stack.pop()
            
            if not node:
                continue
            
            if visited:
                # Now both children are processed
                left_sum = max(0, path_sum.get(node.left, 0))
                right_sum = max(0, path_sum.get(node.right, 0))
                
                # Update global max
                res = max(res, left_sum + right_sum + node.val)
                
                # Store best downward path (return value in recursion)
                path_sum[node] = max(left_sum, right_sum) + node.val
            else:
                # Postorder: push node again as visited, then children
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return res




                    




            


    
        
                

        