class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nsg=[]
        res1=[n]*n
        for i in range(len(heights)-1,-1,-1):
            while nsg and heights[nsg[-1]]>=heights[i]:
                nsg.pop()
            if len(nsg)==0:
                res1[i]=n
            else:
                res1[i]=nsg[-1]
            nsg.append(i)
        res2=[-1]*n
        psg=[]
        for i,x in enumerate(heights):
            while psg and heights[psg[-1]]>=x:
                psg.pop()
            if len(psg)==0:
                res2[i]=-1
            else:
                res2[i]=psg[-1]
            psg.append(i)
        ans=-1
        for i in range(n):
            width = res1[i] - res2[i] - 1
            ans = max(ans, heights[i] * width)
        return ans

