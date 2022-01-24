#User function Template for python3
#problem link: https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1#
def findMin(root,dn):
    node=root
    minm=root
    p=None
    prev=p
    while(node):
        if node.data<minm.data and node!=dn:
            prev=p
            minm=node
        p=node
        node=node.next

    return prev,minm
    
def flatten(root):
    if root==None: return None
    node=head
    dummy_node=Node(-1)
    
    #Attach dumy node to end of flat list
    while(node.next):
        node=node.next
    node.next=dummy_node
    
    #start populating the flatten list in sroted order
    node=root
    ptr=dummy_node
    while(node!=dummy_node):
        #find min node
        p,minm=findMin(node,dummy_node)
        #detach minm from list
        btm=minm.bottom
        nxt=minm.next
        minm.next=None
        minm.bottom=None
        #attach minm to prt:
        ptr.bottom=minm
        ptr=ptr.bottom
        #put btm in minm pos
        if p and btm: 
            p.next=btm
            btm.next=nxt
        if p and not btm:
            p.next=nxt
        if btm and not p:
            btm.next=nxt
            node=btm
        if not p and not btm:
            node=nxt
       
       

    return dummy_node.bottom
    
    
    