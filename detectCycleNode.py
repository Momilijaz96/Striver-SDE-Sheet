# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==head:
            return head
        node=head
        while(node):
            if not isinstance(node.val,tuple):
                node.val=(node.val,1)
                node=node.next
            else:
                return node
        return None