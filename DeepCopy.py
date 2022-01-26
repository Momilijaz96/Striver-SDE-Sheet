"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        
        dc_head=Node(head.val)
        dc_node=dc_head
        node=head
        orig=[]
        dc=[dc_head]
        while(node):
            if node.next:
                temp=Node(node.next.val)
                dc_node.next=temp
                dc_node=dc_node.next
                dc.append(dc_node)
            orig.append(node)
            node=node.next

        #update random pointer
        dc_node=dc_head
        node=head
        while(node):
            if node.random:
                idx=orig.index(node.random)
                dc_node.random=dc[idx]
            else: dc_node.random=None
            node=node.next
            dc_node=dc_node.next
        return dc_head
            
            
            
            
            
            
            
            
            