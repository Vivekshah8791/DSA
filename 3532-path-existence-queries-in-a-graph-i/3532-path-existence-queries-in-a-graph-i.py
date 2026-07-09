class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp=[0]*n
        for i in range(1,n):
            if nums[i]-nums[i-1]<=maxDiff:
                comp[i]=comp[i-1]
            else:
                comp[i]=comp[i-1]+1
        ans=[]
        for u,v in queries:
            if comp[u]==comp[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans