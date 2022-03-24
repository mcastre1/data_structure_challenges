from itertools import cycle
from Node import Node

def cycle_check(node):
    '''
    Function checks whether a linked list has a cycle
    '''
    nodes_seen = []

    while node.nextnode: # If the current node has a next_node continue iterating.
        if node in nodes_seen:
            return True

        nodes_seen.append(node) # Keep track of seen nodes.
        node = node.nextnode # Swap current node with next node.

    return False




# First test
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle

print(cycle_check(a))

# Second test
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print(cycle_check(x))