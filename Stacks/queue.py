# FIFO
# Queue() create a new queue
# enqueue() adds a new item to the rear of the queue
# dequeue() removes the front item from the queue
# isEmpty() tests to see whether te queue is empty
# size() returns the numbers of items in the queue

class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(1)
print(q.dequeue())