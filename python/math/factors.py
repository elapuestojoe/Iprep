def getFactors(n):
    if(n==0):
        return [1]
    array = []
    stack = []
    for i in range(1, int(n**(1/2)+1)):
        if(n % i == 0):
            array.append(i)
            if(n//i != i): #Square root
                stack.append(n//i)
            
    while(len(stack)>0):
        array.append(stack.pop())
    return array

print(getFactors(100))
print(getFactors(2))
print(getFactors(1))
print(getFactors(0))