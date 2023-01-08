class Multistack:
    def __init__(self,size,noofstack) :
        self.list = [None]*size
        self.size_of_list = size
        self.size_of_stack = size//noofstack
        self.no_of_stacks = noofstack 
        self.sizes_of_stack = [-1]* noofstack

    # stack no index start from 1,2,3
    def indexofstack(self,stacknumber):
        index = self.size_of_stack * (stacknumber - 1) + self.sizes_of_stack[stacknumber-1 ]
        return index 
    
    def isempty(self,stacknumber):
        if self.sizes_of_stack[stacknumber-1] == -1:
            return True
        else:
            return False

    def isfull(self,stacknumber):
        if self.sizes_of_stack[stacknumber-1] == self.size_of_stack-1:
            return True
        else:
            return False
    def enqueue(self,stacknumber,value):
        if not self.isfull(stacknumber):
           offset = self.indexofstack(stacknumber)
           self.list[offset+1] = value
           self.sizes_of_stack[stacknumber-1] +=1
           return "data is inserted"
        else:
            return "stack is already full"
    
    def dequeue(self,stacknumber):
        if not self.isempty(stacknumber):
            popindex = self.indexofstack(stacknumber)
            popdata = self.list[popindex]
            self.list[popindex] = None
            self.sizes_of_stack[stacknumber-1] -= 1
            return popdata
        else:
            return "stack is empty"
    
    def __str__(self):
        print(self.list)
        return "stack printed"
    

multistack = Multistack(9,3)
multistack.enqueue(1,12)
multistack.enqueue(2,112)
multistack.enqueue(1,121)
multistack.enqueue(1,120)
print(multistack.enqueue(1,125))
print(multistack)
print(multistack.dequeue(1))
print(multistack)
print(multistack.dequeue(3))



    

