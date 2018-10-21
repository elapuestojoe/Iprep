def solution(A):
    maxFruit = 0
    for i in range(len(A)):
        leftBasketElement = None
        leftBasketCount = 0
        rightBasketElement = None
        rightBasketCount = 0

        listFinished = False

        for j in range(i, len(A)):
            fruit = A[j]
            
            if(j == len(A) - 1):
                listFinished = True

            if(leftBasketElement is None):
                leftBasketElement = fruit
                leftBasketCount += 1
            elif(fruit == leftBasketElement):
                leftBasketCount += 1
            elif(rightBasketElement is None):
                rightBasketElement = fruit
                rightBasketCount += 1
            elif(fruit == rightBasketElement):
                rightBasketCount += 1
            
            else:
                if(leftBasketCount + rightBasketCount > maxFruit):
                    maxFruit = leftBasketCount + rightBasketCount
                break
        #If list was exhausted then there is no point in searching after that, either we already have the max or this subsequence is the max
        if(listFinished):
            if(leftBasketCount + rightBasketCount > maxFruit):
                maxFruit = leftBasketCount + rightBasketCount
            break 
    return maxFruit
        