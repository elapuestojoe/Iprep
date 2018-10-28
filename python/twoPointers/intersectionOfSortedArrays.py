'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        iA = 0
        iB = 0
        results = []
        while(iA < len(A) and iB < len(B)):
            if(A[iA] == B[iB]):
                results.append(A[iA])
                iA+=1
                iB+=1
            elif(A[iA] < B[iB]):
                iA+=1
            else:
                iB+=1
        return results