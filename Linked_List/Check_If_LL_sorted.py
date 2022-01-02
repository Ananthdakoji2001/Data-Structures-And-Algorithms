def check_sorted(l):
    prev=l.head
    curr=l.head.next
    while curr!=None:
        if prev.val<=curr.val:
            prev=curr
            curr=curr.next
        else:
            return False
    return True
  
  
  
  
  
