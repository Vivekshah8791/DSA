# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,k):
        if root is None:
            return
        self.solve(root.left,k)
        self.count+=1
        if self.count==k:
            self.ans=root.val
            return 
        self.solve(root.right,k)       
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=None
        self.count=0
        self.solve(root,k)
        return self.ans