// Using sliding pointer method

def reverse(l):
    r=None        # r holds the previous noder
    q=None        # q holds the present node to be linked to previous
    p=l.head      # p hold the next node
    l.tail=p      # making reversed LL tail --> LL head of present LL.
    while p!=None:
        r=q
        q=p
        p=p.next
        q.next=r   # making link from present node to previous node
    l.head = q
reverse(l)
