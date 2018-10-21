#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def extraDataSolution(string : str) -> bool:
    '''
    Uses a HashMap to detect repeated characters
    Time Complexity O(n)
    Space Complexity O(n)
    '''
    charDictionary = {}
    for c in string:
        if(c not in charDictionary):
            charDictionary[c] = True
        else:
            return False
    return True

def noExtraDataSolution(string : str) -> bool:
    '''
    Sorts the string to detect duplicates
    Time Complecity O(n log n)
    Space Complexity O(1)
    '''
    charList = []
    for c in string:
        charList.append(c)
    charList = sorted(charList)
    for i in range(1, len(charList)):
        if(charList[i] == charList[i-1]):
            return False

    return True

#Driver code
a = "abcdefg"
b = "abcdefa"

print(extraDataSolution(a))
print(extraDataSolution(b))

print(noExtraDataSolution(a))
print(noExtraDataSolution(b))
