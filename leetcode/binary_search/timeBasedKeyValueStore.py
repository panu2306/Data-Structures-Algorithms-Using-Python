class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.time_map):
            self.time_map[key] = []

        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # key is not present in time_map - 
        if(key not in self.time_map):
            return ""
         
        # when key is present there are again three conditions:
            # 1. timestamp is present
            # 2. timestamp is not present but less than given timestamp exists
            # 3. timestamp is not present and also less than given timestamp value also doesn't exist -> return ""
        
        # using binary search to find for above 
        left, right = 0, len(self.time_map[key]) - 1
        while(left <= right):
            mid = (left + right) // 2
            if(self.time_map[key][mid][1] == timestamp):
                return self.time_map[key][mid][0]
            if(self.time_map[key][mid][1] < timestamp):
                left = mid + 1
            else:
                right = mid - 1
        return "" if right < 0 else self.time_map[key][left-1][0]
        
timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))    # return "bar"
print(timeMap.get("foo", 3))    # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
print(timeMap.set("foo", "bar2", 4)) # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         # return "bar2"
print(timeMap.get("foo", 5))         # return "bar2"

