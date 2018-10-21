
def mergeSort(array):
    if(len(array) <= 1):
        return array

    half = len(array) // 2
    lowerArray = mergeSort(array[:half])
    upperArray = mergeSort(array[half:])

    lowerSize = len(lowerArray)
    upperSize = len(upperArray)
    i = 0
    j = 0

    result = []
    while(i < lowerSize and j < upperSize):
        
        if(lowerArray[i] < upperArray[j]):
            result.append(lowerArray[i])
            i += 1
        else:
            result.append(upperArray[j])
            j += 1

    while(i < lowerSize):
        result.append(lowerArray[i])
        i+=1
    
    while(j < upperSize):
        result.append(upperArray[j])
        j+=1
    return result

    

array = [9,5,6,7,8]
sortedArray = mergeSort(array)

print(sortedArray)