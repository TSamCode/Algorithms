from LinkedList import LinkedList

def intersection(linkedListOne, linkedListTwo):
    
    # We need to determine which of the linked lists is longer, and to also know the difference in their lengths
    shorterList = linkedListOne if len(linkedListOne) < len(linkedListTwo) else linkedListTwo
    longerList = linkedListOne if len(linkedListOne) >= len(linkedListTwo) else linkedListTwo
    lengthDiff = len(longerList) - len(shorterList)

    # We first check the last element of the two lists and if they do not match then we know they don't intersect
    if linkedListOne.tail.data is not linkedListTwo.tail.data:
        return False

    # We will begin our iteration over the linked lists from their heads
    shorterListNode = shorterList.head
    longerListNode = longerList.head

    # We then want to move the longerList forwards by the number of nodes extra it has compared to the shorter list
    # This means the longerList and shorterList then have equal numbers of remaining nodes
    for _ in range(lengthDiff):
        longerListNode = longerListNode.next

    # As long as the nodes are not equal then we progress them one position further
    # This will therefore return the matching nodes, stopping at the tail
    # If the tail is not equal then this will be caught in the first if statement above
    while shorterListNode.data is not longerListNode.data:
        shorterListNode = shorterListNode.next
        longerListNode = longerListNode.next
    
    return longerListNode

testOne = LinkedList([1,2,3,4,5,6,7,8,9,10])
testTwo = LinkedList([15,14,13,12,11,6,7,8,9,10])

#print(testOne.tail.data is testTwo.tail.data)

print(intersection(testOne, testTwo))