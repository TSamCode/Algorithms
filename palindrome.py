# Function to see if a string is some permutation of a palindrome
from collections import Counter

def permPalindrome(string):
    # creates a list of characters
    stringChars = [char for char in string.lower() if char.isalpha()]
    # create a dictionary containing the count of each character in the string
    charCounts = Counter(stringChars)
    # We add up the number of characters that appear an odd number of times
    oddCharCounts = sum(1 for char, count in charCounts.items() if count%2)
    # If all characters appear an even number of times, or there is only one odd count then a palindrome is possible
    return oddCharCounts <= 1

print(permPalindrome('Thomas'))