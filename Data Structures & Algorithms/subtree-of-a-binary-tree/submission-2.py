# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self,p,q):
        if p is None and q is  None:
            return True
        elif p is None or q is None:
            return False
        elif p.val!=q.val:
            return False
        
        return (self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right))

          
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        p=root
        q=subRoot

        if p is None:
            return False

        check=self.isSameTree(p,q)

        if check==True:
            return True
        else:
            return (self.isSubtree(p.left,q) or self.isSubtree(p.right,q))

        