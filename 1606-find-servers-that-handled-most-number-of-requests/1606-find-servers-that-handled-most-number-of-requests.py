class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        servers = SortedList(range(k))
        freq = {i: 0 for i in range(k)}
        pq = []
        for i in range(len(arrival)):
            while pq and pq[0][0] <= arrival[i]:
                time, s = heapq.heappop(pq)
                servers.add(s)
            if not servers:
                continue
            idx = servers.bisect_left(i % k)
            if idx == len(servers):
                idx = 0
            server = servers.pop(idx)
            freq[server]+=1
            heapq.heappush(pq,[arrival[i]+load[i],server])
        maxi=max(freq.values())
        return [key for key,value in freq.items() if value==maxi]
                    
