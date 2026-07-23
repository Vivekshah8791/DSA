class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dirt= [
            (0,1), (0,-1),
            (1,0), (-1,0),
            (1,1), (1,-1),
            (-1,1), (-1,-1)
        ]
        if grid[0][0]==1:
            return -1
        queue=deque()
        queue.append([0,0,1])
        grid[0][0]=1
        while queue:
            i,j,d=queue.popleft()
            if i==row-1 and j==col-1:
                return d
            for dr,dc in dirt:
                nr,nc=i+dr,j+dc
                if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                    queue.append([nr,nc,d+1])
                    grid[nr][nc]=1
        return -1