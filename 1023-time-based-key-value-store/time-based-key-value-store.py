
def search(times, timestamp):
    low, high = 0, len(times) - 1
    while low <= high:
        med = low + (high - low) // 2
        if med + 1 < len(times):
            if times[med][0] < timestamp and times[med + 1][0] > timestamp:
                return med
        if times[med][0] == timestamp:
            return med
        if times[med][0] > timestamp:
            high = med - 1
        else:
            low = med + 1
    return med
class TimeMap:
    #key -> timestamp (always unique per key) in AVL -> value
    def __init__(self):
        self.map = {} #key -> list with unique in order timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        med = search(self.map[key], timestamp)
        if med == 0:
            if self.map[key][med][0] > timestamp:
                return ""
        return self.map[key][med][1] 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)