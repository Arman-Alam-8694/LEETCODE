# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow=head
        fast=head
        prev=head
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        if prev==slow:
            head=prev.next
            return head
        else:
            prev.next=slow.next
            slow.next=None
            return head
        
        

        
        