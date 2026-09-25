class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        ans = []
        def solve(substr, news):
            if substr == "":
                ans.append(news[:-1])
                return
            for word in wordDict:
                l = len(word)
                if substr.startswith(word):
                    solve(substr[l:], news + word + " ")
        solve(s, "")
        return ans