# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root is None:
            return [0,0]
        leftsum,leftcount=self.solve(root.left)
        rightsum,rightcount=self.solve(root.right)
        sumi=root.val+leftsum+rightsum
        nodes=1+leftcount+rightcount
        if sumi//nodes==root.val:
            self.count+=1
        return [sumi,nodes]
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0
        self.solve(root)
        return self.count