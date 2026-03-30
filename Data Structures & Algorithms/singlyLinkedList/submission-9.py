class Node:
    def __init__(self):
        self.val = None
        self.next = None
    def __init__(self,value):
        self.val = value
        self.next = None
    def setValue(self,value):
        self.val = value
    def getValue(self):
        return self.value
    def setNext(self,Next):
        self.next = Next
    def getNext(self):
        return self.next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur= cur.next
        return -1
        
    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next= self.head.next
        self.head.next = newNode
        if newNode.next == None:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        if not self.head.next:
            return False
        i = 0
        cur = self.head
        while i < index:
            i+=1
            cur = cur.next
            if not cur:
                return False
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
