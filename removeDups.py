from LinkedList import LinkedList

def removeDups(linkedList):
    currentNode = linkedList.head
    previousNode = None
    seenValues = set()

    while currentNode:
        # If the current node is a duplicate then we skip this node by linking the previous node to the 'next' node of the current position
        if currentNode.data in seenValues:
            previousNode.next = currentNode.next
        # If we have not seen this we add it to seen nodes
        else:
            seenValues.add(currentNode.data)
            previousNode = currentNode
        # We then move the node forwards by 1 position
        currentNode = currentNode.next
    # Once we have finished all the nodes we set the previous position to be the tail
    linkedList.tail = previousNode

    return linkedList

def main():
    testList = [1,2,3,4,5,6,1,5,3,5,2,7,8,9]
    testLinkedList = LinkedList(testList)
    print(testLinkedList)
    print(removeDups(testLinkedList))

if __name__ == '__main__':
    main()