class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know={}
        for key,val in knowledge:
            know[key]=val
        ans=""
        i=0
        while i<len(s):
            if s[i]=='(':
                curr=i+1
                while curr<len(s) and s[curr]!=')':
                    curr+=1
                if s[i+1:curr] in know:
                    ans+=know[s[i+1:curr]]
                else:
                    ans+='?'
                i=curr+1
            else:
                ans+=s[i]
                i+=1
        return ans

            

