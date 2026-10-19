# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue=deque()
        queue.append(root)
        level=1
        ans=-1
        maxi=float('-inf')
        while queue:
            size=len(queue)
            total=0
            for _ in range(size):
                node=queue.popleft()
                total+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if maxi<total:
                maxi=total
                ans=level
            elif maxi==total:
                ans=min(ans,level)
            level+=1
        return ans
            
                