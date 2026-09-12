class Solution:
    def solve(self,index,buy,t,limit,prices,dp):
        if t==limit or index==len(prices):
            return 0
        if dp[index][buy][t]!=-1:
            return dp[index][buy][t]
        pick=0
        notpick=0
        sell=0
        notsell=0
        if buy==1:
            pick=-prices[index]+self.solve(index+1,0,t,limit,prices,dp)
            notpick=self.solve(index+1,1,t,limit,prices,dp)
        else:
            sell=prices[index]+self.solve(index+1,1,t+1,limit,prices,dp)
            notsell=self.solve(index+1,0,t,limit,prices,dp)
        dp[index][buy][t]=max(pick,notpick,sell,notsell)
        return dp[index][buy][t]
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=[[[-1 for _ in range(k+1)]for _ in range(2)]for _ in range(len(prices))]
        return self.solve(0,1,0,k,prices,dp)