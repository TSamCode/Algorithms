class Node():

    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous
    
    def __str__(self):
        return str(self.data)

class LinkedList():
    
    # Create a linked list with a single head node
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data is not None:
            self.addMultiple(data)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        length = 0
        currentNode = self.head
        while currentNode:
            length += 1
            currentNode = currentNode.next
        return length

    def __str__(self):
        data = [str(item) for item in self]
        return ' --> '.join(data)

    # method to insert into a linked list
    def add(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail

    def addMultiple(self, data):
        for item in data:
            self.add(item)

    def addToBeginning(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.head = Node(data, self.head)

    def removeFromHead(self):
        if self.head is not None:
            originalHead = self.head
            self.head = self.head.next
        return originalHead