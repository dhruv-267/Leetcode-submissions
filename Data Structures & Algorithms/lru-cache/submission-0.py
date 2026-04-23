class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next ,self.right.prev = self.right, self.left

    def remove(self, node):
        templeft , tempright = node.prev, node.next
        templeft.next, tempright.prev = tempright ,templeft

    def add(self, node):
        previous = self.right.prev
        node.prev, node.next = previous, self.right
        previous.next , self.right.prev = node, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if len(self.cache)> self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
    

        
