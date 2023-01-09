class platestack:
    def __init__(self,thres) :
        self.list = []
        self.thres = thres
    
    def isempty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    
    # stack index start from  0
    def isempty_stackindex(self,stackindex):
        if len(self.list[stackindex]) == 0:
            return True
        else:
            return False
    
    def isfull_stackindex(self,stackindex):
        if len(self.list[stackindex]) == self.thres:
            return True
        else:
            return False
    
    def enqueue(self,item):
        if len(self.list)>0 and not self.isfull_stackindex(len(self.list)-1):
            self.list[len(self.list)-1].append(item)
        else:
            self.list.append([item])
    
    def pop(self):
        res = []
        while not self.isempty():
            if len(self.list[-1]) > 0:
                popitem  = self.list[-1].pop()
                res.append(popitem)
            else:
                self.list.pop(-1)
        return res
    
    def pop_atindex(self,stackindex):
        if not self.isempty() and len(self.list) > stackindex:
           if len(self.list[stackindex]) >0: 
                popitem = self.list[stackindex].pop()
                if len(self.list[stackindex]) == 0:
                    self.list.pop(stackindex)
                
                return popitem
        else:
            return False
            
            
        

plate = platestack(3)
plate.enqueue(1)
plate.enqueue(2)
plate.enqueue(3)
plate.enqueue(4)
plate.enqueue(5)

print(plate.pop_atindex(1))
print(plate.pop_atindex(11))
print(plate.pop())