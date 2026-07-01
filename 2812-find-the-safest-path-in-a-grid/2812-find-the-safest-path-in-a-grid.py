class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dist=[[-1 for _ in range(col)]for _ in range(row)]
        queue=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    dist[r][c]=0
                    queue.append((r,c))
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c=queue.popleft()
            for dx,dy in dir:
                dr,dc=r+dx,c+dy
                if 0<=dr<row and 0<=dc<col and dist[dr][dc]==-1:
                    dist[dr][dc]=dist[r][c]+1
                    queue.append((dr,dc))
        def canreach(limit):
            if dist[0][0]<limit:
                return False
            queue=deque([])
            queue.append((0,0))
            visited={(0,0)}
            while queue:
                r,c=queue.popleft()
                if r==row-1 and c==col-1:
                    return True
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < row and
                        0 <= nc < col and
                        (nr, nc) not in visited and
                        dist[nr][nc] >= limit
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return False
        ans=0
        low=0
        high=max(max(row) for row in dist)
        while low<=high:
            mid=low+(high-low)//2
            if canreach(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans