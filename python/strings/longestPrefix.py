def longestCommonPrefix(A):
    if(len(A) == 0):
        return ""
    
    maxPossibleIndex = len(A[0])
    for i in range(1, len(A)):
        if(len(A[i]) < maxPossibleIndex):
            maxPossibleIndex = len(A[i])
            
    index = 0
    finished = False
    while(index < maxPossibleIndex and not finished):
        char = A[0][index]
        for stringIndex in range(1, len(A)):
            string = A[stringIndex]
            if(string[index] != char):
                finished = True    
                break
        if(not finished):
            index += 1
    print(index, maxPossibleIndex)
    return A[0][:index]
            
A = [ "abcd", "abde", "abcf" ]
print(longestCommonPrefix(A))