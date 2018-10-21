class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        
        #in Python ints can be any size
        #however, in another language this would have to be done using a long
        intA = int(A)
        a = (intA & (intA-1))
        
        if(a == 0):
            return 1
        else:
            return 0