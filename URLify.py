def URLify(string):
    newString = string.replace(" ", "%20")
    return newString

print(URLify('Thomas Adams 1993'))