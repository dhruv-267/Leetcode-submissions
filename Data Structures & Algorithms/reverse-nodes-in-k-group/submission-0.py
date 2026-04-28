# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        grpPrev = dummy

        while True:
            kth = self.getKth(grpPrev,k)
            if not kth:
                break
            nextgrpprev = grpPrev.next
            nextgrp = kth.next
            kth.next = None
            self.reverseList(grpPrev.next,nextgrp)
            grpPrev.next = kth
            grpPrev = nextgrpprev
        
        return dummy.next


    def reverseList(self,root,pre):
        prev = pre
        while root:
            nxt = root.next
            root.next = prev
            prev = root
            root = nxt
        return prev
    
    def getKth(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr



    