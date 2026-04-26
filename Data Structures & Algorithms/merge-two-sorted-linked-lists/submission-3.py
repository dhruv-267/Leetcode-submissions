# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = list1
        head2 = list2

        dummy = ListNode(200,None)
        head = dummy

        while head1 and head2:
            if head1.val<=head2.val:
                dummy.next = head1
                dummy = dummy.next
                head1=head1.next
            else:
                dummy.next= head2
                dummy = dummy.next
                head2 = head2.next
        
        if head1:
            dummy.next = head1
        else:
            dummy.next = head2

        return head.next

        


























        
        
        '''
        dummy = ListNode()
        tail = dummy  #tail pointer to append values

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
        '''