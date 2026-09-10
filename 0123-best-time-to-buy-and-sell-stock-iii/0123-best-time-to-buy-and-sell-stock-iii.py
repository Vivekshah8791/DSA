class Solution:
    def solve(self,index,buy,limit,prices,dp):
        if limit==2 or index==len(prices):
            return 0
        if dp[index][buy][limit]!=-1:
            return dp[index][buy][limit]
        pick=0
        notpick=0
        sell=0
        notsell=0
        if buy==1:
            pick=-prices[index]+self.solve(index+1,0,limit,prices,dp)
            notpick=self.solve(index+1,1,limit,prices,dp)
        else:
            sell=prices[index]+self.solve(index+1,1,limit+1,prices,dp)
            notsell=self.solve(index+1,0,limit,prices,dp)
        dp[index][buy][limit]=max(pick,notpick,sell,notsell)
        return dp[index][buy][limit]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n)]
        return self.solve(0,1,0,prices,dp)