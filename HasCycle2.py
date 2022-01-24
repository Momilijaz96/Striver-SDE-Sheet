# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None: return None
        if head.next==None: return False
        slow=head
        fast=head
        while(fast):
            fast=fast.next
            if fast:
                fast=fast.next
            slow=slow.next
            if fast==slow:
                return True
        return False
    