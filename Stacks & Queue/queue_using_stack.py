class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enQueue(self,item):
        self.s1.append(item)
    
    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return 
        
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        
        else:
            return self.s2.pop()


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())