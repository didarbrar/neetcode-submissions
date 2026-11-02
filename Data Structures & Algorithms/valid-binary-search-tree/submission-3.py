# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        is_valid=True

        def dfs(node,min_value,max_value):
            nonlocal is_valid
            if node is None:
                return 
            if node.val<=min_value or node.val>=max_value:
                is_valid=False
            dfs(node.left,min_value,node.val)
            dfs(node.right,node.val,max_value)
        dfs(root,float('-inf'),float('inf'))
        return is_valid


        