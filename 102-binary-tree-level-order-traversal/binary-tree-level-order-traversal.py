# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        stack = deque([root])
        result = []
        while stack:
            n = len(stack)
            curr = []
            for _ in range(n):
                node = stack.popleft()
                if node and node.left:
                    stack.append(node.left)
                if node and node.right:
                    stack.append(node.right)
                curr.append(node.val)
            result.append(curr)
        return result


        