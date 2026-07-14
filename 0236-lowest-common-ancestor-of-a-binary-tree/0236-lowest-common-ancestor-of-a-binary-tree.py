# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self,root,p,q):
        if root is None:
            return None
        if root==p or root==q:
            return root
        left=self.solve(root.left,p,q)
        right=self.solve(root.right,p,q)
        if left!=None and right!=None:
            return root
        elif left==None:
            return right
        else:
            return left
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)