def isSubstring(wordOne, wordTwo):
    if wordOne in wordTwo:
        return True
    else:
        return False

# x is a roation of y is we can find the string x within the string yy
def rotation(wordOne, wordTwo):
    if len(wordOne) == len(wordTwo) != 0:
        return isSubstring(wordOne,wordTwo+wordTwo)
    else:
        return False

print(rotation('erbottlewat','waterbottle'))