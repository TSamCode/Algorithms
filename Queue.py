class Queue():

    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) == 0:
            return None
        itemToRemove = self.queue[0]
        del self.queue[0]
        return itemToRemove