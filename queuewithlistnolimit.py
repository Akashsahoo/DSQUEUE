class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self) :
        values = [str(i) for i in self.items]
        return  "\n".join(values)
    def isempty(self):
        if self.items == []:
           return True
        return False

    def peek(self):
        if not self.isempty():
            return self.items[0]
    
    def enqueue(self,value):

        self.items.append(value)
    
    def dequeue(self):
        if not self.isempty():
            return self.items.pop(0)
        return "Queue is empty"

queue = Queue()
print(queue.isempty())
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue)
print(queue.dequeue())
print(queue.peek())


