'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

    Example:
    Given input array A = [1,1,2],
    Your function should return length = 2, and A is now [1,2].
'''

def removeDuplicates(A):
    # Validation
    if(len(A)==0):
        return []

    nextI = 1
    currentElement = A[0]
    for i in range(1, len(A)):
        if(A[i] > currentElement):
            currentElement = A[i]
            A[i], A[nextI] = A[nextI], A[i]
            nextI += 1
    return nextI

a = [1,1,2,2,2,3,3,3,3,4]
print(removeDuplicates(a))
print(a)
    