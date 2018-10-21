def compareVersion(A, B):
    a = [int(i) for i in A.split(".")]
    b = [int(i) for i in B.split(".")]
    
    currentIndex = 0
    while(currentIndex < len(a) and currentIndex < len(b)):
        if(a[currentIndex] < b[currentIndex]):
            return -1
        elif(a[currentIndex] > b[currentIndex]):
            return 1
        else:
            currentIndex+=1

    aIterator = currentIndex
    bIterator = currentIndex
    while(aIterator < len(a)):
        if(a[aIterator] > 0):
            return 1
        aIterator+=1
    while(bIterator < len(b)):
        if(b[bIterator] > 0):
            return -1
        bIterator+=1
    return 0


# print(compareVersion("0.1", "1.1"))
# print(compareVersion("1.13.5", "1.13"))
# print(compareVersion("10.1", "10.1"))
print(compareVersion("8.88888888888888888888888888888", "8.888888888888888"))
print(compareVersion("1.0", "1"))
print(compareVersion("1.0.1", "1"))