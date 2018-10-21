'''
Given a sorted array of integers a, find an integer x from a such that the value of

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

is the smallest possible (here abs denotes the absolute value).
If there are several possible answers, output the smallest one.

For a = [2, 4, 7], the output should be
absoluteValuesSumMinimization(a) = 4.
'''
def absoluteValuesSumMinimization(a):
    #Solution is median of a if a has odd elements
    sizeOfA = len(a)
    if(sizeOfA&1):
        return a[sizeOfA//2]
    else:
        #if a has even elements, we have to check which one gets better results
        leftSum = 0
        leftElement = a[(sizeOfA//2)-1]
        for i in range((sizeOfA//2)-1):
            leftSum += leftElement - a[i]
        rightSum = 0
        rightElement = a[sizeOfA//2]
        for i in range(sizeOfA//2, len(a)):
            rightSum += a[i] - rightElement
        
        if(rightSum < leftSum):
            return rightElement
        else:
            return leftElement
        