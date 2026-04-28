# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grpPrev = dummy

        while True:
            kth = self.getKth(grpPrev,k)
            if not kth:
                break
            
            nextgrp = kth.next
            kth.next = None
            thisgrp = grpPrev.next
            self.reverseList(thisgrp,nextgrp)
            grpPrev.next = kth
            grpPrev = thisgrp

        return dummy.next

    

    def reverseList(self,cur,pre):
        prev = pre
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
    
    def getKth(self,root,k):
        while root and k>0:
            root = root.next
            k-=1
        return root