class Pair:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.length = 0
        self.table = [None]*capacity
    
    def hash(self,key):
        return key  % self.size 
    
    def resize(self) -> None:
        oldmap = self.table
        self.size = self.size * 2
        self.table = [None] * self.size
        self.length = 0

        for pairs in oldmap:
            if pairs:
                self.insert(pairs.key, pairs.value)

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while self.table[index] != None:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            index += 1
            index = index % self.size
        
        self.table[index] = Pair(key,value)
        self.length += 1
        
        if self.length >= self.size // 2:
            self.resize()
        return

    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.table[index]!=None:
            if self.table[index].key == key:
                return self.table[index].value
            index += 1
            index = index % self.size

        return -1 

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.table[index]!=None:
            if self.table[index].key == key:
                self.table[index] = None
                self.length -= 1
                return True
            index += 1
            index = index % self.size

        return False

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.size

    

