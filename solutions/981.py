class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        m = self.m
        m[key].append([timestamp, value])
        
    
    def get(self, key: str, timestamp: int) -> str:
        m = self.m
        if len(m[key]) == 0: return ""
        left, right = 0, len(m[key])-1
        maxprev = -1
        while left <= right:
            mid = (left+right)//2
            if m[key][mid][0] <= timestamp:
                maxprev = mid
            if m[key][mid][0]==timestamp:
                return m[key][mid][1]
            elif m[key][mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return m[key][maxprev][1] if maxprev != -1 else ""

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)