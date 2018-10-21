def getPrimes(n):
    primes = []
    l = [i for i in xrange(2, n)]
    
    while(len(l)>0):
        prime = l[0]
        primes.append(prime)
        temp = []
        for i in xrange(1,len(l)):
            if(l[i] % prime != 0):
                temp.append(l[i])
        l = temp

    return primes

def binarySearch(number, numberArray):
    
    start = 0
    end = len(numberArray)-1
    midPoint = (start + (end-1))/2
    while(end >= start):
        
        if(numberArray[midPoint] == number):
        
        if(numberArray[midPoint] > number):
            end = midPoint - 1
        else:
            start = midPoint + 1
        
        midPoint = (start + (end-1))//2
        
    return False

print(getPrimes(100))

print(binarySearch(5, [1,2,3,4,5,6,7,8,9]))

print(binarySearch(100, [1,2,3,4,5,6,7,8,9]))

print(getPrimes(4))