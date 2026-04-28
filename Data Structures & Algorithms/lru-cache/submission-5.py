class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next ,self.right.prev = self.right, self.left

    def remove(self, root):
        root_left,root_right = root.prev,root.next
        root_left.next , root_right.prev = root_right , root_left
        del self.cache[root.key]

    def add(self,key,value):
        node = ListNode(key,value)
        self.cache[key] = node
        node_left , node_right = self.right.prev, self.right
        node_left.next, self.right.prev = node , node
        node.next ,node.prev = self.right, node_left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            val = node.value
            self.remove(node)
            self.add(key,val)
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(key,value)
        else:
            if len(self.cache) == self.capacity:
                self.remove(self.left.next)
            self.add(key,value)

            

        
