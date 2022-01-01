from Queue import queue

class stack:
    def __init__(self):
        self.q1=queue()
        self.q2=queue()
        self.length=0
        
    def push(self,val):
        self.q1.enqueue(val)
        self.length +=1
        
    def pop(self):
        curr=self.q1.first
        while curr!=self.q1.last:
            self.q2.enqueue(self.q1.dequeue())
            curr=curr.next
        holding_pointer=self.q1.dequeue()
        self.q1, self.q2=self.q2, self.q1  // changing reference q1-->q2 , q2-->q1
        self.length -=1
        return holding_pointer
        
        
        
        
        
        
        
