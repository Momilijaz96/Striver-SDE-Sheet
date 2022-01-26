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
        if root==None: return None
        node=root.next
        tree=Tree(root.val)
        tree_ptr=tree
        while(node):
            if tree_ptr.val<=node.val:
                tree_ptr.right=Tree(node.val)
                tree_ptr=tree_ptr.right
            elif tree_ptr.val>node.val:
                tree_ptr.left=Tree(node.val)
                tree_ptr=tree_ptr.left
            node=node.next
        return tree

