def getSum(self, A, accumulator):
    if(A is None):
        accumulator += 0
    elif(A.left is None and A.right is None):
        accumulator +=  A.val
    else:
        accumulator += A.val
        left = self.getSum(A.left, accumulator*10)
        right = self.getSum(A.right, accumulator *10)
        
        accumulator += left
        accumulator += right
    return accumulator
def sumNumbers(self, A):
    return self.getSum(A, 0) % 1003