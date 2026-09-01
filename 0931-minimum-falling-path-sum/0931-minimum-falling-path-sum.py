class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        prev=[-1]*row
        for c in range(col):
            prev[c]=matrix[row-1][c]
        for r in range(row-2,-1,-1):
            curr=[-1]*row
            for c in range(col):
                down=prev[c]
                dialeft=float("inf")
                diaright=float("inf")
                if c>0:
                    dialeft=prev[c-1]
                if c+1<col:
                    diaright=prev[c+1]
                curr[c]=matrix[r][c]+min(down,dialeft,diaright)
            prev=curr
        return min(prev)
