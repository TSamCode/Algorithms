from simpleStack import Stack

class SortedStack(Stack):

    def __init__(self):
        # By initialising we give the stack the functions: peek, isEmpty, pop, len
        super().__init__()
        self.temporaryStack = Stack()

    # The standard Stack push() function is not suitable for the Sorted Stack
    # It must be amended to remove the items from the Stack until we can then append the item
    def push(self, item):
        # If the sorted stack is empty then we can just add the item to the stack
        # If the item is smaller than the last item in the SortedStack then we can append it
        # We need to use the push function from the super() class
        if self.isEmpty() or item < self.peek():
            # We then force it to use the push function from the simple stack by using super() here
            super().push(item)
        # If the Stack isn't empty or the item is not the smallest then we can't just append it
        else:
            # We look at the top item of the stack
            # If it is larger than the item then we add it to the temporary stack
            # We repeat this until the top item of the stack is larger than the item to be added
            while self.peek() is not None and item > self.peek():
                self.temporaryStack.push(self.pop())
            # Once the top of the stack is larger than the item we can then push the item onto the stack
            super().push(item)
            # We then need to return the items from the temporary stack back into the sorted stack until the temporary stack is empty
            while self.temporaryStack.isEmpty() is False:
                super().push(self.temporaryStack.pop())

if __name__ == '__main__':
    sortedStackTest = SortedStack()
    sortedStackTest.push(1)
    sortedStackTest.push(2)
    sortedStackTest.push(3)
    sortedStackTest.push(4)
    sortedStackTest.push(5)
    print(sortedStackTest.items)
