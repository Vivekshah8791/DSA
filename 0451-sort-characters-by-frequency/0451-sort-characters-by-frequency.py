class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        arr=[]
        for key,val in freq.items():
            arr.append([val,key])
        arr.sort(key=lambda x:-x[0])
        ans=""
        for n,ch in arr:
            ans+=ch*n
        return ans