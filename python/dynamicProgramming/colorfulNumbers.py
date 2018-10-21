
def colorful(A):
    solutions = {}
    products = []
    while(A > 9):
        products.append(A % 10)
        A = A // 10
    products.append(A)

    while(len(products) > 2):
        tempArr = []
        
        for i in range(len(products) - 1):
            currentVal = products[i]
            nextVal = products[i+1]

            if(currentVal in solutions):
                return False
            else:
                solutions[currentVal] = True

            tempArr.append(currentVal*nextVal)

        if(products[-1] in solutions):
            return False
        else:
            solutions[products[-1]] = True

        products = tempArr
    
    # Compute last values
    for value in products:
        if(value in solutions):
            return False
        else:
            solutions[value] = True
    
    return len(products) == 1 or products[0] * products[1] not in solutions

print(colorful(3245))
print(colorful(3235))
print(colorful(12))
print(colorful(1))