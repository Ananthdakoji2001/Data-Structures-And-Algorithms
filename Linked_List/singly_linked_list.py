class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        self.tail.next=new_node
        self.tail=new_node
        self.length+=1

    def prepend(self,val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        self.length += 1

    def insert(self,i,val):
        if i==0:
            self.prepend(val)
        elif i>=self.length:
            self.append(val)
        else:
            new_node=Node(val)
            pointer=1
            curr=self.head
            while pointer!=i:
                curr=curr.next
                pointer+=1
            new_node.next=curr.next
            curr.next=new_node
        self.length += 1

    def remove(self,value):
        if self.head.val==value:
            self.head=self.head.next
        else:
            curr = self.head
            while curr.val!=value:
                previous=curr
                curr=curr.next
            previous.next=curr.next
        self.length+=1

    def print(self):
        curr=self.head
        while curr !=None:
            print(curr.val)
            curr=curr.next

l=LinkedList()






