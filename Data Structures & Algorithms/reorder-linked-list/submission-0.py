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

        second = slow.next #important :Fast will be none.. start of second array will be slow.next
        slow.next = None #important End first list by updating slow.next to None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev
        first = head

        while second:
            firstnxt , secondnxt = first.next , second.next
            first.next = second
            second.next = firstnxt
            first = firstnxt
            second = secondnxt
        

