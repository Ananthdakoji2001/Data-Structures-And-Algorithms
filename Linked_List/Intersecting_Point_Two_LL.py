//creating LL1
l1=LinkedList()

l1.append(1)
l1.append(3)
l1.append(5)
l1.append(8)
l1.append(12)

//creating LL2
l2=LinkedList()

l2.append(67)
l2.append(23)
l2.append(22)

// making LL2 intersect at value - 5
l2.tail.next=l1.head.next.next

//Now LL looks like 

     1-->3-->5-->8-->12
            /    
67-->23-->21

//stack1 for storing addrs of each and every node in LL1, similiarly for stack2

s1=stack()
s2=stack()

p=l1.head
while p:
    s1.push(id(p))
    p=p.next

p=l2.head
while p:
    s2.push(id(p))
    p=p.next


while s1.peek()==s2.peek():   // check from top of stack or we can say reverse order of LL if different addrs are found from s1 and s2 it means end of intersection
    p=s1.pop()
    s2.pop()

#import ctypes
import ctypes

a = ctypes.cast(p, ctypes.py_object).value

# display
print("At Value - ", a.val)
