class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        for n in grid:
            arr.extend(n)
        row=len(grid)
        col=len(grid[0])
        n=len(arr)
        k=k%n
        arr=arr[n-k:n]+arr[:n-k]
        r=0
        i=0
        while r<row:
            for c in range(col):
                grid[r][c]=arr[i]
                i+=1
            r+=1
        return grid
        
