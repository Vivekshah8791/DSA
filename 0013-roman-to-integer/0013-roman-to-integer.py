class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"CD":400,"C":100,"D":500,"M":1000}
        number=0
        i=0
        n=len(s)
        while i<n:
            if i+1<n and dict[s[i]]<dict[s[i+1]]:
                number=number+dict[s[i+1]]-dict[s[i]]
                i=i+2
            else:
                number+=dict[s[i]]
                i+=1
        return number
