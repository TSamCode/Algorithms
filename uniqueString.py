def uniqueChar(string):
    return (len(string) == len(set(string)))

userInput = input('Enter a string --> ')

while userInput != '':
    print(uniqueChar(userInput))
    userInput = input('Enter a string --> ')

