class Solution:
    def solve(self,s,index,n):
        if index==n:
            return s[::]
        i=0
        news=""
        while i<len(s):
            count=1
            while i+1<len(s) and s[i]==s[i+1]:
                count+=1
                i+=1
            news+=str(count)+s[i]
            i+=1
        return self.solve(news,index+1,n)
    def countAndSay(self, n: int) -> str:
        return self.solve("1",1,n)