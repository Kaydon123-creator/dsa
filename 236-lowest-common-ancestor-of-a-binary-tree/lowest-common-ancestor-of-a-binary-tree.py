class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def lca(node):
            if not node:
                return None 

            if node == p or node == q:
                return node

            l = lca(node.left)
            r = lca(node.right)

            if l and r:
                return node 

            return l if l else r 

        return lca(root)
