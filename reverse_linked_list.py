from Node import Node

def reverse(head):
    '''
    Reverses the links between nodes in a singly linked list.
    '''
    previous = None # Keeps track of the previous node.

    while head.nextnode: # While there is a next node, we continue iterating
        temp = head         # These 2 "temp nodes" keep track of the current and next node
        next = head.nextnode

        if previous:    # If we have a previous then we link the current to the previous node.
            head.nextnode = previous

        head = next   # We move into the next node
        previous = temp # And we update the previous with the current node.

    head.nextnode = previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse(a)

print("REVERSED")

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)