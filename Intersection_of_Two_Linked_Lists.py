# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def markNode(self,node):
        if node.val>0:
            node.val=node.val*-1
        else:
            node.val=node.val*-1
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None: return None
        if headB==None: return None
        na=headA
        nb=headB
        int_node=None
        while(na or nb):
            if na:
                if na.val>0:
                    na.val= -1*na.val 
                else:
                    na.val=na.val*-1
                    int_node= na
                    break
            if nb:
                if nb.val>0:
                    nb.val=-1*nb.val
                else:
                    nb.val=nb.val*-1
                    int_node= nb
                    break
            if na: na=na.next
            if nb: nb=nb.next
        #Restore list structure
        na=headA
        nb=headB
        while(na or nb):
            if na:
                na.val= -1*na.val if na.val<0 else na.val
            if nb:
                nb.val= -1*nb.val if nb.val<0 else nb.val
            if na: na=na.next
            if nb: nb=nb.next
        return int_node