# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,key):
        if root is None:
            return root
        if key<root.val:
            root.left=self.solve(root.left,key)
        elif key>root.val:
            root.right=self.solve(root.right,key)
        else:

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            temp=root.right
            while temp.left:
                temp=temp.left
            root.val=temp.val
            root.right=self.solve(root.right,temp.val)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.solve(root,key)