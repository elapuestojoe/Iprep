import math
def justifySpace(emptySpace, nSpaces):
    return math.ceil(emptySpace/nSpaces)

def getWord(stringBuffer, l, currentLineSize):
    spaces = len(stringBuffer)-1
    emptySpace = l - currentLineSize + len(stringBuffer) - 1
    i = 0
    newLine = []
    space = 0
    while(i < len(stringBuffer)-1):
        newLine.append(stringBuffer[i])
        space = justifySpace(emptySpace, spaces)
        newLine.append(" "*space)
        emptySpace-= space
        spaces-=1
        i+=1
        space += len(stringBuffer[i]) + space

    newLine.append(stringBuffer[-1])
    if(space < l):
        newLine.append(" ")
    return "".join(newLine)
def textJustification(words, l):
    results = []
    stringBuffer = []
    currentLineSize = 0
    for word in words:
        wordSize = len(word)
        if(currentLineSize + wordSize <= l):
            stringBuffer.append(word)
            
            currentLineSize += len(word)
            currentLineSize+=1
        else:
            results.append(getWord(stringBuffer, l, currentLineSize))
            
            stringBuffer=[word]
            currentLineSize = len(word)

    if(len(stringBuffer)>0):
        results.append(getWord(stringBuffer, l, currentLineSize))
    return results

words = ["This", "is", "an", "example", "of", "text", "justification."]
print(textJustification(words, 16))

words = ["Two", "words."]
print(textJustification(words, 11))