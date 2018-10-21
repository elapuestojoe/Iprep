'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        count = 1
        element = A[0]
        for i in range(1, len(A)):
            if(count==0):
                count = 1
                element = A[i]
            elif(element == A[i]):
                count += 1
                
            else:
                count -=1
        return element