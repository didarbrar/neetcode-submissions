# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index=0

        root_map={value:i for i,value in enumerate(inorder)}

        def dfs(left,right):
            nonlocal pre_index

            if left>right:
                return None
            
            root_value=preorder[pre_index]
            pre_index+=1
            root=TreeNode(root_value)
            mid=root_map[root_value]

            root.left=dfs(left,mid-1)
            root.right=dfs(mid+1,right)

            return root

        return dfs(0,len(inorder)-1)
        


        