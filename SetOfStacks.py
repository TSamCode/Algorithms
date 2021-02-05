class SetOfStacks():

    def __init__(self, theCapacity):
        self.capacity = theCapacity
        self.stacks = []

    def __str__(self):
        print(self.stacks)

    def push(self, item):
        # If there is a stack and the last stack is not full then we append the item to this stack
        if (len(self.stacks) != 0) and (len(self.stacks[-1]) < self.capacity):
            self.stacks[-1].append(item)
        # If there are no stacks or the last stack is at capacity then we create a new stack (as a list)
        else:
            self.stacks.append([item])
    
    def pop(self):
        # If there are no stacks then we return none from the pop function
        if len(self.stacks) == 0:
            return None
        poppedItem = self.stacks[-1].pop()
        # If we have a list of stacks that isn't empty but the last stack is empty then we delete the empty stack
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            del self.stacks[-1]
        return poppedItem

    def popAt(self, theStackNumber):
        if (theStackNumber < 0) or (theStackNumber >= len(self.stacks)):
            return None
        elif len(self.stacks[theStackNumber]) == 0:
            return None
        else:
            poppedItem = self.stacks[theStackNumber].pop()
            if len(self.stacks[theStackNumber]) == 0:
                del self.stacks[theStackNumber]
            return poppedItem
        
stackOfPlates = SetOfStacks(5)  
stackOfPlates.push(1)
stackOfPlates.push(2)
stackOfPlates.push(3)
stackOfPlates.push(4)
stackOfPlates.push(5)
stackOfPlates.push(6)
stackOfPlates.push(7)
stackOfPlates.push(8)
stackOfPlates.push(9)
stackOfPlates.push(10)
stackOfPlates.pop()
stackOfPlates.popAt(0)
print(stackOfPlates)