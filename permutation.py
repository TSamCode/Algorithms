def permutation(firstInput, secondInput):

    if len(firstInput) != len(secondInput):
        return False

    firstSorted = sorted(firstInput)
    secondSorted = sorted(secondInput)

    for i in range(len(firstSorted)):
        if firstSorted[i] != secondSorted[i]:
            return False
    
    return True
        
firstInput = input('Enter a string --> ')
secondInput = input('Enter another string --> ')

print(permutation(firstInput, secondInput))