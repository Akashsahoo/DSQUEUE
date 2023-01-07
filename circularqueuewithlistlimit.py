class CircularQueue:
    def __init__(self,maxsize):
        self.items = [None]*maxsize
        self.start = -1
        self.top = -1
        self.maxsize = maxsize
    def print(self) :
        values = [i for i in self.items]
        print(values) 
    def isempty(self):
        if self.start == -1 and self.top == -1:
            return True
        return False
    
    def isfull(self):
        if self.top+1 == self.maxsize and self.start == 0:
            return True
        elif self.top+1 == self.start:
            return True
        return False
    
    def peek(self):
        if not self.isempty():
            return self.items[self.start]
        return 'queue is empty'
    
    def enqueue(self,value):
        if not self.isfull():
            if self.start == -1 and self.top == -1:
                self.start = 0
                self.top = 0
                self.items[self.start] = value
            elif self.top +1 == self.maxsize:
                self.top = 0
                self.items[self.top] = value
            else:
                self.top = self.top + 1
                self.items[self.top] = value
        else:
            print("queue is full")
    
    def dequeue(self):
        if not self.isempty():
            if self.start == self.top:
                data = self.items[self.start]
                self.items[self.start] = None
                self.top = -1
                self.start = -1
                return data
            elif self.start + 1 == self.maxsize:
                data = self.items[self.start]
                self.items[self.start] = None
                self.start = 0
                return data
            else:
                 data = self.items[self.start]
                 self.items[self.start] = None
                 self.start +=  1
                 return data
        else:
            print("queue is empty")


            

circularqueue = CircularQueue(5)

circularqueue.print()

circularqueue.enqueue(1)
circularqueue.enqueue(2)
circularqueue.enqueue(3)
circularqueue.enqueue(4)
circularqueue.print()
print(circularqueue.dequeue())
print(circularqueue.dequeue())
circularqueue.enqueue(1)
circularqueue.enqueue(2)
circularqueue.print()
circularqueue.enqueue(21)
circularqueue.print()
circularqueue.enqueue(22)
circularqueue.print()



     


