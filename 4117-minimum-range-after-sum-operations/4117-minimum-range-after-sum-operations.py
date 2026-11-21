class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        l=[a,b,c]
        l.sort()
        l2=[l[1]+l[2],l[1],l[2]]
        l3=[l[0],l[1],l[0]+l[1]]
        return min(max(l)-min(l),max(l2)-min(l2),max(l3)-min(l3))