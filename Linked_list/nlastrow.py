def nth_node(n,a):
    left_pointer = a 
    right_pointer = a 

    for i in range(n-1):
        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c 
c.next_node = d 

print(nth_node(2,a).value)