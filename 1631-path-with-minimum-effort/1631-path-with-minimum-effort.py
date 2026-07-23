import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col=len(heights[0])
        dirt=[(0,1),(0,-1),(1,0),(-1,0)]
        dist=[[float("inf") for _ in range(col)]for _ in range(row)]
        dist[0][0]=0
        pq=deque=[(0,0,0)]
        while pq:
            effort,r,c=heapq.heappop(pq)
            if effort>dist[r][c]:
                continue
            if r==row-1 and c==col-1:
                return effort
            for x,y in dirt:
                nr,nc=r+x,c+y
                if 0<=nr<row and 0<=nc<col:
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if new_effort<dist[nr][nc]:
                        heapq.heappush(pq,(new_effort,nr,nc))
                        dist[nr][nc]=new_effort
        return 0