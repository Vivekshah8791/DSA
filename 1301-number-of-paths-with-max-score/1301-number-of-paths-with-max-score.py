class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD=10**9+7
        n=len(board)
        dp=[[(-1,0) for _ in range(n)]for _ in range(n)]
        dp[n-1][n-1]=(0,1)
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j]=='X':
                    continue
                dirt=[(1,0),(0,1),(1,1)]
                for x,y in dirt:
                    nr,nc=x+i,y+j
                    if 0<=nr<n and 0<=nc<n:
                        max_score,path=dp[nr][nc]
                        if max_score==-1:
                            continue
                        val=0 if board[i][j] in "SE" else int(board[i][j])
                        score=max_score+val
                        if score>dp[i][j][0]:
                            dp[i][j]=(score,path)
                        elif score==dp[i][j][0]:
                            dp[i][j]=(dp[i][j][0],(dp[i][j][1]+path)%MOD)
        maxi,ways=dp[0][0]
        if maxi==-1:
            return [0,0]
        return [maxi,ways]