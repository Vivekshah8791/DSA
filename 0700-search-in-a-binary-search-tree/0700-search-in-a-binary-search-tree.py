# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,val):
        if root is None:
            return None
        if root.val==val:
            return root
        elif root.val<val:
           return self.solve(root.right,val)
        else:
            return self.solve(root.left,val)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.solve(root,val)