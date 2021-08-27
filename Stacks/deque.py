# Deque() create a new deque that is empty 
# addFront() adds  a new item to the front of the deque
# addRear() adds a new item to the rear of the deque
#removeFront() removes the front item from the deque
# removerear() removes the rear item from the deque
# isEmpty() tests to see whether the deque is empty
# size() returns the size of the deque

class Deque():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items==[]
    
    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

d =Deque()
d.addFront('hello')
d.addRear('world')

print(d.removeFront() + ' ' + d.removeRear())