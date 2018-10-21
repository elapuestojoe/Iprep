def getParent(i):
    
    if(i == 1):
        return "Engineer"
    
    parent = getParent(i//2)
    
    if(i % 2 == 0):
        return parent
    else:
        if(parent == "Engineer"):
            return "Doctor"
        else:
            return "Engineer"
    
def findProfession(level, pos):
    startingPosition = 2**(level-1)
    positionInArr = startingPosition + (pos-1)
    
    return getParent(positionInArr)