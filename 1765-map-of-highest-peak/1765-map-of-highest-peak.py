class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        row=len(isWater)
        col=len(isWater[0])
        height=[[0 for _ in range(col)]for _ in range(row)]
        visited=[[-1 for _ in range(col)]for _ in range(row)]
        queue=deque()
        for i in range(row):
            for j in range(col):
                if isWater[i][j]==1:
                    visited[i][j]=1
                    queue.append([i,j,0])
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c,dist=queue.popleft()
            height[r][c]=dist
            for dx,dy in dir:
                nr=r+dx
                nc=c+dy
                if 0<=nr<row and 0<=nc<col and visited[nr][nc]==-1:
                    visited[nr][nc]=1
                    queue.append([nr,nc,dist+1])
        return height
