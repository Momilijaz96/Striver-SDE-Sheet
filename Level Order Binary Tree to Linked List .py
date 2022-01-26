# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):
        if root==None: return root
        if root.left==None and root.right==None: return LLNode(root.val)

        q=[root]
        head=LLNode(root.val)
        lnode=head
        while(len(q)>0):
            nodes=len(q)
            for _ in range(nodes):
                node=q.pop(0)
                lnode.next=LLNode(node.val)
                lnode=lnode.next
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return head.next


