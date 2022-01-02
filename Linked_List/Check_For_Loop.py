l.tail.next=l.head.next      // just to make a loop

def Check_Loop(l):
    p=l.head
    q=l.head
    while p!=None and q!=None:
        p=p.next            // making 1 step Forward
        q=q.next.next       // making 2 step Forward
        if p==q:
            return True
    return False
  
  
  
  
  
  
  
  
