# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        arr=[]
        queue=deque([root])
        while queue:
            size=len(queue)
            new_arr=[]
            for _ in range(size):
                node=queue.popleft()
                new_arr.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            arr.append(new_arr)
        ans=[]
        for nodes in arr:
            ans.append(nodes[-1])
        return ans
