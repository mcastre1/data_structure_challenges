from Node import Node

def nth_to_last_node(n, head):
    '''
    Returns the nth to last node of a singly linked list
    '''

    nodes = []

    while head.nextnode:
        nodes.append(head)
        head = head.nextnode

    # Takes in the last node and adds it to the nodes list.
    if head.nextnode == None:
        nodes.append(head)


    return nodes[-n]

# Test

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_last_node(2, a)

print(target_node.value)