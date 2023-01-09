class Animal:
    def __init__(self,type,name) :
        self.type = type
        self.name = name
    def __str__(self) -> str:
        return self.name

class queue:
    def __init__(self) :
        self.list = []
    def __str__(self) :
       result =  [str(animal) for animal in self.list]
       print(result) 
       return "Data printed"
    def enqueue(self,animal):
        self.list.append(animal)

    def isempty(self):
        return True if len(self.list)==0 else False 

    def sepecific_dequeue(self,type):
        if not self.isempty() :
            for index in range(len(self.list)):
                 
                if self.list[index].type ==type:
                   popanimal =  self.list.pop(index)
                   return popanimal.type

    def dequeue(self):
        if not self.isempty():
            popanimal =  self.list.pop(0)
            return popanimal.name


Dog1 = Animal('Dog','Dog1') 
Cat1 = Animal('Cat','Cat1')
Dog2 = Animal('Dog','Dog2') 
Cat2 = Animal('Cat','Cat2')
Dog3 = Animal('Dog','Dog3')
Cat3 = Animal('Cat','Cat3')
Cat4 = Animal('Cat','Cat4')
Dog4 = Animal('Dog','Dog4')
Cat5 = Animal('Cat','Cat5')

queueanimal = queue()
queueanimal.enqueue(Dog1)
queueanimal.enqueue(Dog2)
queueanimal.enqueue(Cat1)
queueanimal.enqueue(Dog3)
queueanimal.enqueue(Cat2)
queueanimal.enqueue(Dog4)
queueanimal.enqueue(Cat3)
queueanimal.enqueue(Cat4)

print(queueanimal)
print(queueanimal.dequeue())
print(queueanimal)
print(queueanimal.sepecific_dequeue('Cat'))
print(queueanimal)

             
