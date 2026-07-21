class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        news = '1' + s + '1'
        segments = []
        i = 0
        while i < len(news):
            j = i
            while j < len(news) and news[j] == news[i]:
                j += 1
            segments.append((news[i], j - i))
            i = j
        ans = ones
        for i in range(1, len(segments) - 1):
            if(
                segments[i][0] == '1'
                and segments[i - 1][0] == '0'
                and segments[i + 1][0] == '0'
            ):
                gain = segments[i - 1][1] + segments[i + 1][1]
                ans = max(ans, ones + gain)
        return ans