import simpleStack

class Queue():

    def __init__(self):
        self.inStack = simpleStack.Stack()
        self.outStack = simpleStack.Stack()

    def __str__(self):
        print(self.inStack.items)
        print(self.outStack.items)

    def add(self, item):
        self.inStack.push(item)

    def remove(self):
        # For remove we need to move the items from inStack to outStack and reverse their order
        # This is done by repeatedly taking the last item from the inStack and appending it to the outStack
        if len(self.outStack) == 0:
            while (len(self.inStack) != 0):
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

