class Stack():

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()


    def isEmpty(self):
        return (len(self.items) == 0)

class StackMinimum(Stack):

    def __init__(self):
        super().__init__()
        self.minValue = Stack()

    def push(self, value):
        super().push(value)
        if len(self.minValue.items) == 0:
            self.minValue.push(value)
        elif value <= self.minimumValue():
            self.minValue.push(value)
    
    def pop(self):
        value = super().pop()
        if value == self.minimumValue():
            self.minValue.pop()
        return value

    def minimumValue(self):
        return self.minValue.items[-1]

testStackMin = StackMinimum()
testStackMin.push(1)
testStackMin.push(3)
testStackMin.push(5)
testStackMin.push(7)
print(testStackMin.minimumValue())