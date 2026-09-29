class Solution:
    def solve(self,r,c,count,grid,dp):
        if r>=len(grid) or c>=len(grid[0]):
            return False
        count+=1 if grid[r][c]=='(' else -1
        if count<0:
            return False
        if r==len(grid)-1 and c==len(grid[0])-1:
            return count==0
        if (r,c,count) in dp:
            return dp[(r,c,count)]
        dp[(r,c,count)]=self.solve(r,c+1,count,grid,dp) or self.solve(r+1,c,count,grid,dp)
        return dp[(r,c,count)]
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        dp={}
        return self.solve(0,0,0,grid,dp)