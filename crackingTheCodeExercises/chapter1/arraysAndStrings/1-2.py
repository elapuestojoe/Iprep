#Write a code to reverse a C-Style String. (C-String means that "abcd" is represented as five characters, including the null character.)

def reverseCString(string: str) -> str:
    '''
    Reverse a C-Style String
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    #Convert string to C-Style String
    cString = list(string)
    cString.append(None)

    startIndex = 0
    endIndex = len(cString) - 2

    while(startIndex < endIndex):
        cString[startIndex], cString[endIndex] = cString[endIndex], cString[startIndex]

        startIndex += 1
        endIndex -= 1
    return cString

#Driver code
a = "I am a C String"
print(reverseCString(a))

