from LinkedList import LinkedList, Node

class Animal():
    
    numberOfAnimals = 0

    @classmethod
    def addAnimal(cls):
        cls.numberOfAnimals += 1
    
    def __init__(self, theName):
        Animal.addAnimal()
        self.timeAdmitted = self.numberOfAnimals
        self.name = theName

    def __str__(self):
        print(self.name)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class AnimalShelter(LinkedList):

    def enqueue(self, theAnimal):
        # We create a Node for the specific animal
        # We then add this Node to the animal shelter linked list (this will be the new tail for the linked list)
        theAnimalNode = Node(theAnimal)
        self.add(theAnimalNode)

    # If we want to dequeue any animal then we just need to remove the head from the linked list and return this head
    def dequeueAny(self):
        return self.removeFromHead()

    def dequeueCat(self):
        currentNode = self.head
        previousNode = None
        while currentNode is not None:
            if isinstance(currentNode.data, Cat):
                previousNode.next = currentNode.next
                return currentNode
            previousNode = currentNode
            currentNode = currentNode.next
        return None

    def dequeueDog(self):
        currentNode = self.head
        previousNode = None
        while currentNode is not None:
            if isinstance(currentNode.data, Dog):
                previousNode.next = currentNode.next
                return currentNode
            previousNode = currentNode
            currentNode = currentNode.next
        return None


if __name__ == '__main__':
    cat1 = Cat('Winston')
    cat2 = Cat('Flissy')
    dog1 = Dog('Amber')
    dog2 = Dog('Maisy')
    shelter = AnimalShelter()
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)
    
    currentNode = shelter.head
    print(currentNode.data)
    