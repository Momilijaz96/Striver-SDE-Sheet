# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLength(self,root):
        node=root
        length=0
        while(node):
            length+=1
            node=node.next
        return length
        
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None: return None
        length=self.findLength(head)
        if k==length: return head.next
        if k>length:  return head
        idx=(length-k)
        count=1
        node=head
        while(node):
            if count==idx:
                par_target=node
            node=node.next
            count+=1

        par_target.next=par_target.next.next
        return head