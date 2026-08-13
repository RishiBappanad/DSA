class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.reference = {}
        self.size = 0
        self.capacity = capacity
        self.last = None
        self.start = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.put(key, self.map[key].val)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            curr = Node(value)
            self.map[key] = curr
            self.reference[curr] = key
            if self.size == 0:
                self.start, self.last = curr, curr
                self.size += 1
                return
            if self.size == self.capacity:
                if self.capacity == 1:
                    ref = self.reference[self.start]
                    del self.map[ref]
                    del self.reference[self.start]
                    self.start, self.last = curr, curr
                    return
                last = self.last
                self.last = last.prev
                self.last.next = None
                ref = self.reference[last]
                del self.reference[last]
                del self.map[ref]
            else:
                self.size += 1
        else:
            curr = self.map[key]
            curr.val = value
            if curr == self.start:
                return
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            else:
                self.last = curr.prev
        curr.next = self.start
        self.start.prev = curr
        self.start = curr
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)