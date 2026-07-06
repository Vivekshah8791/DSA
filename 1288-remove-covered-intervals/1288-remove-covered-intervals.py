class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans=0
        for i in range(len(intervals)):
            start,end=intervals[i]
            covered=False
            for j in range(len(intervals)):
                if i==j:
                    continue
                second_start,second_end=intervals[j]
                if second_start<=start and end<=second_end:
                    covered=True
                    break
            if not covered:
                ans+=1
        return ans
