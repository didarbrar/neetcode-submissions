# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced=True

        def dfs(node):
            nonlocal is_balanced

            if node is None:

                return 0

            left_depth=dfs(node.left)
            right_depth=dfs(node.right)

            if abs(right_depth - left_depth) > 1:
                is_balanced = False
            return 1+max(left_depth,right_depth)
        dfs(root)
        return is_balanced
        