
l.tail.next=l.head   // to make circular linked list l
node=l.head.next.next
def check_for_circular_LL(l,node):
    if node.next ==None:
        return False
    else:
        curr=node.next

    while curr:       // if curr==None then jumps out of the loop, circular ll does not contains any Null values
        if curr==node:
            return True
        curr=curr.next
    return False
  
  
  
  
  
  
  
  
  
  
  
  
