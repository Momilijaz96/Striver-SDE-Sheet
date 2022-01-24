# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None: return None
        node=head
        while(node):
            if node.val!='seen':
                node.val='seen'
            else:
                return True
            node=node.next
        return False