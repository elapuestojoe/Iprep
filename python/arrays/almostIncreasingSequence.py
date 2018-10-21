'''
Given a sequence of integers as an array, 
determine whether it is possible to obtain 
a strictly increasing sequence by removing 
no more than one element from the array.
'''

def findNonIncreasingElement(sequence):
    for i in range(1, len(sequence)):
        if(sequence[i] <= sequence[i-1]):
            return i
    return len(sequence)

def checkSequenceIgnoringIndex(sequence, index):
    i = 0
    while(i < len(sequence)-1):
        if(i == index):
            i += 1
        j = i + 1
        if(j == index):
            j += 1
        
        if(j < len(sequence) and sequence[j] <= sequence[i]):
            return False
        i+=1
    return True
def almostIncreasingSequence(sequence):
    #Find a conflicting item
    nonIncreasingIndex = findNonIncreasingElement(sequence)
    if(nonIncreasingIndex == len(sequence)):
        return True
    else:
        
        possibleConflict1 = nonIncreasingIndex
        possibleConflict2 = possibleConflict1 - 1
        return checkSequenceIgnoringIndex(sequence, possibleConflict1) or checkSequenceIgnoringIndex(sequence, possibleConflict2)


print(almostIncreasingSequence([1,2,3,4,5]))
print(almostIncreasingSequence([1,2,1,2]))
print(almostIncreasingSequence([10,1,2,3,4,5]))
print(almostIncreasingSequence([2,3,4,5,1]))
print(almostIncreasingSequence([1,1]))

print(almostIncreasingSequence([1,2,3,4,3,6]))

''' Would be interesting to check this Kotlin solution
fun almostIncreasingSequence(sequence: MutableList<Int>): Boolean {
        var countFalse = 0
    
        for (i in 1 until sequence.size) {
            if (sequence[i] <= sequence[i-1]) {
                countFalse++
                if(i != 1)
                    if(sequence[i] <= sequence[i-2])
                        if(i+1 < sequence.size && sequence[i+1] <= sequence[i-1])
                            countFalse++
            }
            if (countFalse >= 2)
                return false
        }
        return true
    }
'''