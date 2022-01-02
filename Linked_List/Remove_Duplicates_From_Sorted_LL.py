// note : l should be sorted
def remove_duplicates(l):
    prev=l.head
    curr=l.head.next
    while curr!=None:
        if prev.val==curr.val:
            prev.next=curr.next
            curr=curr.next
        else:              //if the values are not same then move forward
            prev=curr
            curr=curr.next

            
            
            
            
