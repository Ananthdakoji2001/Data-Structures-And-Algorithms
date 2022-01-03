
// using two pointers p,q
// p move 2 steps
// q moves 1 step
// by doing this, if p reaches to end of LL then q should be at Middle (q=2*p)

def middle_element(l):         //l is Linkedlist
    p=l.head
    q=l.head
    while p:
        p=p.next
        if p:
            p=p.next
        if p:
            q=q.next
    return q.val
