class Solution:
    def minOperations(self, s: str) -> int:
        sorted_s="".join(sorted(s))
        if s==sorted_s:
            return 0
        if len(s)<=2:
            return -1
        n=len(sorted_s)
        mini=sorted_s[0]
        maxi=sorted_s[-1]
        if mini==s[0] or maxi==s[-1]:
            return 1
        elif mini==s[n-1] and maxi==s[0] and mini not in s[1:-1] and maxi not in s[1:-1]:
            return 3
        else:
            return 2



        
        