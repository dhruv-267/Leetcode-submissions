# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 and l2:
            carry , rem = divmod(l1.val+l2.val+carry,10)
            tail.next = ListNode(rem)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                carry , rem = divmod(l1.val+carry,10)
                tail.next = ListNode(rem)
                tail = tail.next
                l1 = l1.next
        elif l2:
            while l2:
                carry , rem = divmod(l2.val+carry,10)
                tail.next = ListNode(rem)
                tail = tail.next
                l2 = l2.next

        if carry:
            tail.next = ListNode(carry)
            
        return dummy.next

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        dummy = ListNode()
        cur = dummy

        carry = 0
        while carry or l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, dig = divmod(val1+val2+carry,10)

            cur.next = ListNode(dig)


            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        """

        