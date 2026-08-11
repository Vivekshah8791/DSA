class LFUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.pq=[]
        self.time=0
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.time+=1
        v,f,t=self.cache[key]
        self.cache[key]=[v,f+1,self.time]
        heapq.heappush(self.pq,[f+1,self.time,key])
        return v

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        self.time+=1
        if key in self.cache:
            v,f,t=self.cache[key]
            self.cache[key]=[value,f+1,self.time]
            heapq.heappush(self.pq,[f+1,self.time,key])
            return
        
        if len(self.cache)>=self.capacity:
            while self.pq:
                f,t,k=heapq.heappop(self.pq)
                if k in self.cache and self.cache[k][1]==f and self.cache[k][2]==t:
                    del self.cache[k]
                    break
        self.cache[key]=[value,1,self.time]
        heapq.heappush(self.pq,[1,self.time,key])
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)