class ManyStacks():

    def __init__(self, theStackSize, theNumberStacks):
        self.numberStacks = theNumberStacks
        self.stackSize = theStackSize
        self.sizes = [0] * self.numberStacks
        self.array = [0] * self.numberStacks * self.stackSize

    def validStackNumber(self, theStackNumber):
        if theStackNumber >= self.numberStacks:
            raise ValueError(theStackNumber, 'Is not a valid stack number!')

    def push(self, theStackNumber, value):
        self.validStackNumber(theStackNumber)
        if self.isStackFull(theStackNumber):
            raise ValueError(theStackNumber, 'This stack is already full! Push failed.')
        self.array[self.topOfStackIndex(theStackNumber)] = value
        self.sizes[theStackNumber] += 1

    def pop(self, theStackNumber):
        self.validStackNumber(theStackNumber)
        if self.isStackEmpty(theStackNumber):
            raise ValueError(theStackNumber, 'This stack is already empty! Pop failed.')
        self.sizes[theStackNumber] -= 1
        self.array[self.topOfStackIndex] = 0


    def isStackFull(self, theStackNumber):
        self.validStackNumber(theStackNumber)
        return (self.sizes[theStackNumber] == self.stackSize)
    
    def isStackEmpty(self, theStackNumber):
        self.validStackNumber(theStackNumber)
        return (self.sizes[theStackNumber] == 0)
    
    def topOfStackIndex(self, theStackNumber):
        self.validStackNumber(theStackNumber)
        offset = theStackNumber * self.stackSize
        return offset + self.sizes[theStackNumber]