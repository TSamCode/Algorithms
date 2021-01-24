def stringCompression(string):
    compressed = ''
    for char in string:
        # If the compressed string is empty or this character is different to the previous character
        # Then we ppend to the compressed string the new character and begin its counter at 1
        if len(compressed) == 0 or char != compressed[-2]:
            compressed += char
            compressed += '1'
        # If the new character is equivalent to the last character then we just increase its counter by 1
        # and replace this value at the end of the compressed string
        elif char == compressed[-2]:
            counter = int(compressed[-1]) + 1
            compressed = compressed[:-1] + str(counter)
    
    # If the compressed string is no shorter than the original then we just return the original string
    if len(compressed) >= len(string):
        return string
    else:
        return compressed

print(stringCompression('aabcccccaaa'))