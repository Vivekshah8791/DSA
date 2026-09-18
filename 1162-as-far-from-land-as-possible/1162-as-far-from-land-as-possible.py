class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        queue=deque([])
        watercount=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    queue.append([i,j])
                else:
                    watercount+=1
        if watercount==0 or len(queue)==0:
            return -1
        ans=0
        dic=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue and watercount:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dx,dy in dic:
                    nr,nc=r+dx,c+dy
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                        grid[nr][nc]=1
                        queue.append([nr,nc])
                        watercount-=1
            ans+=1
        return ans if watercount==0 else -1