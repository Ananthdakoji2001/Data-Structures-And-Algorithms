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
      
      
      
      
      
      
  
