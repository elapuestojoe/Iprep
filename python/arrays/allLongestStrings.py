def allLongestStrings(inputArray):
    maxChars = 0
    returnArray = []
    for i in range(len(inputArray)):
        currentString = inputArray[i]
        if(len(currentString) > maxChars):
            maxChars = len(currentString)
            returnArray = [currentString]
        elif(len(currentString) == maxChars):
            returnArray.append(currentString)
    return returnArray

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))