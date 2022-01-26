#Problem Link; https://binarysearch.com/room/buffer-overflow-vFaRJZVMhA
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,root):
        if root==None: return None
        if root.next==None: return root
        p=None
        c=root
        while(c):
            cn=c.next
            c.next=p
            p=c
            c=cn
        return p

    def solve(self, root, k):
        if root==None: return None
        rev_root=self.reverse(root)
        count=0
        node=rev_root
        while(count<=k):
            if count==k:
                return node.val
            node=node.next
            count+=1
        

