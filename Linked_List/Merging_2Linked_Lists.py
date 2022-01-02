from implementation import Linkedlist

l=LinkedList()    // LL-1
l.append(1)
l.append(3)
l.append(4)

l1=LinkedList()   // LL-2
l1.append(-5)
l1.append(-1)
l1.append(50)

l2=LinkedList()  // output LL
p=l.head
q=l1.head

while  p!= None or q!=None:
    if p and p.val<=q.val:
        l2.append(p.val)
        p=p.next
    else:
        if q:
            l2.append(q.val)
            q=q.next
            
l2.print()








