class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0

    def enqueue(self,val):
        new_node=Node(val)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1

    def dequeue(self):

        if self.length==0:
            return None
        else:
            holding_pointer=self.first
            self.first=self.first.next
            self.length -= 1
            return holding_pointer.val


    def print(self):
        curr=self.first
        while curr !=None:
            print(curr.val)
            curr=curr.next



