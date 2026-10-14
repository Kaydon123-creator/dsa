class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(timestamp, value)]
            return 
        self.dic[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        values = self.dic[key]

        left = 0 
        right = len(values) - 1
        result = -1
        while left <= right:
            mid = (left+right)//2
            if values[mid][0] <= timestamp:
                result = values[mid][1] 
                left = mid + 1 
            else:
                right = mid -1
        return result if result != -1 else ""


        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)