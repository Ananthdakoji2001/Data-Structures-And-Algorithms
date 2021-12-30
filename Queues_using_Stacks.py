class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class stack:
    def __init__(self):
        self.top=None
        self.length=0

    def push(self,val):
        new_node=Node(val)
        if self.length==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.length+=1

    def pop(self):
        holding_pinter=self.top
        self.top=self.top.next
        self.length-=1
        return holding_pinter.val

    def peek(self):
        return self.top.val

    def print(self):
        curr=self.top
        while curr!=None:
            print(curr.val)
            curr=curr.next


class Queue:
    def __init__(self):
        self.s1=stack()
        self.s2=stack()
        self.length=0

    def enqueue(self,val):
        self.s1.push(val)
        self.length +=1

    def dequeue(self):
        curr=self.s1.top
        while curr!=None:
            self.s2.push(curr.val)
            self.s1.pop()
            curr=curr.next
        holding_pointer=self.s2.pop()
        curr = self.s2.top
        while curr!=None:
            self.s1.push(curr.val)
            self.s2.pop()
            curr=curr.next

        self.length -=1
        return holding_pointer



    def print(self):
        curr=self.s1.top
        while curr!=None:
            print(curr.val)
            curr=curr.next
