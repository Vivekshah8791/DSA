class Solution:
    def dfs(self,grid,best,row,col,r,c,health):
        if health<1:
            return False
        if r==row-1 and c==col-1:
            return health>=1
        if best[r][c]>=health:
            return False

        best[r][c]=health
        dirt=[(0,1),(0,-1),(1,0),(-1,0)]
        for x,y in dirt:
            nr,nc=x+r,y+c
            if 0<=nr<row and 0<=nc<col:
                newhealth=health-grid[nr][nc]
                if self.dfs(grid,best,row,col,nr,nc,newhealth):
                    return True
        return False

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        health-=grid[0][0]
        if health<1:
            return False
        row =len(grid)
        col=len(grid[0])
        best=[[-1 for _ in range(col)]for _ in range(row)]
        return self.dfs(grid,best,row,col,0,0,health)