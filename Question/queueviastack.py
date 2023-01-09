class stack:
    def __init__(self):
        self.list = []
    
    def isempty(self):
        if self.list == []:
            return True
        return False
    
    def pop(self):
        if not self.isempty():
            popitem = self.list.pop()
            return popitem
        return "stack is empty"

    def push(self,item):
        self.list.append(item)
           
class QueueviaStack:
    def __init__(self):
        self.stack1 = stack()
        self.popstack2 = stack()
    
    def isempty(self):
        if self.stack1.isempty():
           return True
        else:
            return False

    def enqueue(self,value):
        self.stack1.push(value)
       
    
    def dequeue(self):
        if not  self.isempty():
            while  not self.stack1.isempty():
                popitem = self.stack1.pop()
                self.popstack2.push(popitem)
            dequeueelement = self.popstack2.pop()
            while not self.popstack2.isempty():
                popitem = self.popstack2.pop()
                self.stack1.push(popitem)
            return dequeueelement
        else:
            return "stack is empty"


queue = QueueviaStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

        
    

    


        