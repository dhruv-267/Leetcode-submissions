class ListNode:
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next , self.right.prev = self.right , self.left

    def remove(self, root):
        rootleft , rootright = root.prev , root.next
        rootleft.next , rootright.prev = rootright ,rootleft
        del self.cache[root.key]

    def add(self, key, value):
        if len(self.cache) == self.capacity:
            self.remove(self.left.next)
        
        node = ListNode(key,value)
        self.cache[key] = node
        node_left = self.right.prev
        node_left.next , self.right.prev = node,node
        node.prev , node.next = node_left,self.right


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.value
            self.remove(node)
            self.add(key,val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.add(key,value)
        else:
            self.remove(self.cache[key])
            self.add(key,value)


        
