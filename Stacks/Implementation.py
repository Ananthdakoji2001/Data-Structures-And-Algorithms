class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

        
class stack:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0

    def peek(self):
        return self.top.val

    def push(self,val):
        new_node=Node(val)
        if self.top==None:
            self.top=new_node
            self.bottom=new_node
        else:
            top=self.top
            self.top=new_node
            new_node.next=top

    def print(self):
        curr=self.top
        while curr!=None:
            print(curr.val)
            curr=curr.next

    def pop(self):
        holding_pointer=self.top
        self.top=self.top.next
        return holding_pointer
      
      
      
      
      
      
  
