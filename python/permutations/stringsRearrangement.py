def differFromOneCharOnly(a, b):
    diff = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            diff+=1
    return diff == 1

def arraySatisfiesCondition(inputArray):
    for i in range(0, len(inputArray)-1):
        if(not differFromOneCharOnly(inputArray[i], inputArray[i+1])):
            return False
    return True

def permute(array, l, r):
    if(l == r):
        return arraySatisfiesCondition(array)
    else:
        for i in range(l, r+1):
            array[l], array[i] = array[i], array[l]
            result = permute(array, l+1, r)
            if(result):
                return True
            array[l], array[i] = array[i], array[l]
    return False

def stringsRearrangement(inputArray):
    return permute(inputArray, 0, len(inputArray)-1)

arr = ["ff", 
 "gf", 
 "af", 
 "ar", 
 "hf"]

print(stringsRearrangement(arr))