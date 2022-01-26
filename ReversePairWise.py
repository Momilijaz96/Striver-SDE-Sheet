# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swap_next_pointers(self,p,f,s):
        if f and s:
            sn=s.next
            f.next=sn
            s.next=f
            if p: p.next=s
    def solve(self, root):
        if root==None: return None
        if root.next==None: return root
        f=root
        s=f.next
        p=None
        new_root=s
        while(f and s):
            self.swap_next_pointers(p,f,s)
            p=f
            f=f.next
            s=f.next if f else None
        return new_root
        
