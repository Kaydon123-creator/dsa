# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag = False
        if not root:
            return []
        stack = deque([root])
        result = []
        while stack:
            n = len(stack)
            curr = []
            for _ in range(len(stack)):
                node = stack.popleft()
                curr.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if zigzag:
                result.append(curr[::-1])
                zigzag = False
            else:
                result.append(curr)
                zigzag = True
        return result
            

        