class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[["#" for _ in range(n)]for _ in range(m)]
        grid[0][0]="."
        ans=[]
        if n>1 and m>1:
            for i in range(m):
                grid[i][1]="."
            for j in range(1,n):
                grid[m-1][j]="."
            for k in range(m):
                T=""
                for l in range(n):
                    T+=grid[k][l]
                ans.append(T)
            return ans
            
        
        else :
            grid=[["." for _ in range(n)]for _ in range(m)]
            for k in range(m):
                T=""
                for l in range(n):
                    T+=grid[k][l]
                ans.append(T)
            return ans
        
                    
            
