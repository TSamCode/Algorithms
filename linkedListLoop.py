from LinkedList import LinkedList

def detectLoop(theLinkedList):
     
    nodesObserved = []

    currentNode = theLinkedList.head

    while currentNode:
        if currentNode.data not in nodesObserved:
            nodesObserved.append(currentNode.data)
            currentNode = currentNode.next
        elif currentNode.data in nodesObserved:
            return currentNode
        else:
            return None

print(detectLoop(LinkedList([1,2,3,4,5,6,7,8,5,10,11,13,12])))
print(detectLoop(LinkedList([1,2,3,4,5,6,7,8])))