# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next      # saved reference pointer to second half list
        slow.next = None        # broke list in half
        
        prev = 0
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #prev will give head of reversed node
        
        first ,second = head, prev      #heads of two lists

        while second :                                          #smaller length list : in case of odd list
            firstnxt , secondnxt = first.next , second.next     #save next pointers of both
            first.next = second
            second.next = firstnxt
            first = firstnxt
            second = secondnxt
        








