class Node:
    def __init__(self,value,priorityvalue):
        self.value = value
        self.priority = priorityvalue
    def __str__(self):
        return str(self.value) + str("-priority") + str(self.priority)


class PriorityQueue:
    def __init__(self,size):
        self.size = size+1
        self.lastusedindex = 0
        self.list = [None]*self.size
    def __str__(self):
        for i in range(1,self.lastusedindex+1):
            print(self.list[i])
        return "True"
    def isempty(self):
        if self.lastusedindex == 0:
            return True
        else:
            return False
    def peak(self):
        if not self.isempty():
            return self.list[1]
    def enqueue(self,value,priorityvalue):
        newnode = Node(value=value,priorityvalue=priorityvalue)
        self.list[self.lastusedindex+1] = newnode
        self.lastusedindex = self.lastusedindex + 1
        if self.lastusedindex > 1:
           self.heapifyinsert()
    def dequeue(self):
        if not self.isempty():
            dequeueelement = self.list[1]
            self.list[1] = self.list[self.lastusedindex]
            self.lastusedindex = self.lastusedindex -1
            if self.lastusedindex > 0:
                self.heapifydelete(1)
            return dequeueelement

    def heapifydelete(self,index):
        leftchild = 2 * index
        rightchild = (2 * index) +1
        swapchild = None
        if leftchild <= self.lastusedindex:
            if leftchild == self.lastusedindex:
                if (self.list[leftchild].priority > self.list[index].priority):
                    self.list[leftchild] ,self.list[index] = self.list[index] ,self.list[leftchild]
                    return 
            if self.list[leftchild].priority > self.list[rightchild].priority:
                swapchild = leftchild
            else:
                swapchild = rightchild
            if (self.list[index].priority < self.list[swapchild].priority):
                self.list[swapchild] ,self.list[index] = self.list[index] ,self.list[swapchild]
                self.heapifydelete(swapchild)
        else:
            return 
            
    def heapifyinsert(self):
        index = self.lastusedindex
        parent_index = index //2
        if parent_index > 0:
           
            self.list[parent_index].priority
            while(parent_index >0 and self.list[parent_index].priority < self.list[index].priority):
                self.list[index] ,self.list[parent_index] = self.list[parent_index] ,self.list[index]
                index = parent_index
                parent_index = index //2
                
    



priorqueue = PriorityQueue(10)
# print(priorqueue.isempty())
priorqueue.enqueue('A1',12)
priorqueue.enqueue('A2',11)
priorqueue.enqueue('A3',19)
priorqueue.enqueue('A3',39)
# print(priorqueue) 
print(priorqueue.dequeue())
# print(priorqueue.isempty())
print("After ")
print(priorqueue)   
print(priorqueue.dequeue()) 
print("After ")
print(priorqueue) 

    