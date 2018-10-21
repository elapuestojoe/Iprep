#Redo using trees
def differFromOneCharOnly(a, b):
    diff = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            diff+=1
    return diff == 1
def stringsRearrangement(inputArray):
    inputArray.sort()
    print(inputArray)
    for i in range(0, len(inputArray)-1):
        if(not differFromOneCharOnly(inputArray[i], inputArray[i+1])):
            return False
    return True

inputArray = ["abc", 
 "abx", 
 "axx", 
 "abx", 
 "abc"]

print(stringsRearrangement(inputArray))