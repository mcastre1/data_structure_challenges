class Queue2Stacks(object):
    ''' Implementation of a queue using 2 stacks.
        This works by moving all elements to stack1 when enqueing and
        to stack2 when dequeing'''
    def __init__(self):
        self.stack1 = [] # Keeps track of enqueue
        self.stack2 = [] # Keeps track of dequeue

    def enqueue(self, element):
        # Move all elements in stack2 into the first one. 
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        self.stack1.append(element)

    def dequeue(self):
        # Move all elements in stack1 into the second one.
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()



q = Queue2Stacks()

q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())

