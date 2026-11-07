class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        q = sorted([(queries[i] - x, queries[i], i) for i in range(len(queries))])
        freq = [0] * (n + 1)
        ans = [0] * len(queries)
        left = right = 0
        active = 0
        for start, end, idx in q:
            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1
            ans[idx] = n - active
        return ans