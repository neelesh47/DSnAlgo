class Doubly_linked_list(object):

    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = Doubly_linked_list(1)
b = Doubly_linked_list(2)
c = Doubly_linked_list(3)

a.next_node = b
b.prev_node = a 
b.next_node =c 
c.prev_node = b

