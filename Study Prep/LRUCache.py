class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.order = []

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1
    self.order.remove(key)
    self.order.append(key)
    return self.cache[key]

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.order.remove(key)
    elif len(self.cache) >= self.capacity:
      self.cache.pop(self.order.pop(0))
    self.cache[key] = value
    self.order.append(key)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Test the LRU Cache implementation
lru = LRUCache(2)  # Create cache with capacity 2

# Test operations
lru.put(1, 1)    # cache is {1=1}
lru.put(2, 2)    # cache is {1=1, 2=2}
print(lru.get(1))       # returns 1
lru.put(3, 3)    # evicts key 2, cache is {1=1, 3=3}
print(lru.get(2))       # returns -1 (not found)
lru.put(4, 4)    # evicts key 1, cache is {4=4, 3=3}
print(lru.get(1))       # returns -1 (not found)
print(lru.get(3))       # returns 3
print(lru.get(4))       # returns 4

# Additional test cases to try:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(1, 2)  # What happens when we update an existing key?
print(cache.get(1))  # What value do we get?
cache.put(2, 2)
cache.put(3, 3)
print(cache.get(1))  # Is this the behavior we want?