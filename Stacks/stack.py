#LIFO
#Reverse
#Stack() create new stack -->empty
#oush() add new item to the top of the stack
#pop() removes the top item from stack 
#peek() return the top item from the stack 
#isEmpty test to see whether the stack is empty
#size() return the numberof items on the stack

class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    

s = Stack()
s.push('N')
s.push('e')
s.push('e')
s.push('l')

print(s.peek())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
