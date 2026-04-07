class LLNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.L = LLNode(key=0, val=0)
        self.R = LLNode(key=0, val=0)
        self.L.next = self.R
        self.R.prev = self.L
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.R.prev, self.R

        node.next = nxt # Done
        self.R.prev = node # Node

        node.prev = prev # Done
        prev.next = node # Done

    def get(self, key: int) -> int:
        if key in self.cache:
          self.remove(self.cache[key])
          self.insert(self.cache[key])
          return self.cache[key].val
        
        return -1

          # Updating to most recently used
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
          self.remove(self.cache[key])
        self.cache[key] = LLNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
          lru = self.L.next
          self.remove(lru)
          del self.cache[lru.key]