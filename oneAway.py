# Code to work out if two strings are only one edit different
# We consider an edit to be: add character, remove character, replace character

def oneAway(firstString, secondString):
    # If the string lengths are more than one away from eachother we automatically return false
    if len(firstString) - len(secondString) not in (-1,0,1):
        return False
    # When strings are the same length we want the characters at each index to match apart from at one position
    # We iterate over each index and return True if the number of character differences is 1
    elif len(firstString) == len(secondString):
        differences = 0
        for i in range(len(firstString)):
            if firstString[i] != secondString[i]:
                differences += 1
        return (differences == 1 or differences == 0)
    # If the strings are differing in length by 1 we utilise the replaceCharacter function given below
    elif len(firstString) - len(secondString) == 1:
        return replaceCharacter(firstString, secondString)
    elif len(firstString) - len(secondString) == -1:
        return replaceCharacter(secondString, firstString)

def replaceCharacter(longerString, shorterString):
    # We begin by setting the editMade indicator to False
    # If we come across characters that do not match in the strings then we 'delete' this character from the longer string
    # By doing this we set the editMade indicator to True and prevent any further edits being allowed
    editMade = False
    i, j = 0, 0
    while i < len(longerString) and j < len(shorterString):
        # If the characters dont match but no all previous characters have then we skip a character in the longer string and continue
        if longerString[i] != shorterString[j]:
            # If the characters dont match but a previous set of characters also didnt then we would need more than one edit
            # We return flase in this scenario
            if editMade:
                return False
            else:
                editMade = True
                i += 1
        # If both characters match then we move on to the next index 
        else:
            i += 1
            j += 1
    return True
