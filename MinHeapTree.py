class MinHeap():

    def __init__(self):
        self.heap = []
        self.currentSize = 0

    # Return the smallest item in the heap (found in the first position)
    def peek(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]

    def moveUp(self):
        childIndex = self.currentSize
        parentIndex = (self.currentSize - 1) // 2
        # We then look at the child and parent and swap them if needed
        # This stops once the node is the root or its parent is smaller
        while self.heap[childIndex] < self.heap[parentIndex] and childIndex != 0:
            self.heap[childIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[childIndex]
            childIndex = parentIndex
            parentIndex = (childIndex - 1) // 2

    def push(self, data):
        # We append the data to the heap (in the funal index position)
        self.heap.append(data)
        self.currentSize += 1
        self.moveUp()    

    def moveDown(self):
        parentIndex = 0
        while (parentIndex*2 + 1) <= self.currentSize:
            smallerChild = (parentIndex*2 + 1)
            rightChildIndex = (parentIndex*2 + 2)
            if rightChildIndex <= self.currentSize and self.heap[rightChildIndex] < self.heap[smallerChild]:
                smallerChild = rightChildIndex
            if self.heap[smallerChild] > self.heap[parentIndex]:
                return
            self.heap[smallerChild], self.heap[parentIndex] = self.heap[parentIndex], self.heap[smallerChild]
            parentIndex = smallerChild

    def pop(self):
        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        poppedData = self.heap.pop()
        self.moveDown()
        return poppedData