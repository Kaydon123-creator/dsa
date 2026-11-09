# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.prev = TreeNode()
        self.dummy = self.prev
        self.dfs(root)

    
    def dfs(self,node):
        if not node :
            return  
        self.dfs(node.left) 

        node.left = None 
        nxt = node.right
        self.prev.right = node
        
        self.prev = self.prev.right

        self.dfs(nxt)
        return 
        
    def next(self) -> int:
        if self.hasNext():
            self.dummy = self.dummy.right 
            return self.dummy.val
        else:
            return -1
        

    def hasNext(self) -> bool:
        return True if self.dummy.right  else False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()