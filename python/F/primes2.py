
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
    end = len(numberArray) - 1
    midPoint = start
    while(start <= end):

        print(end)
        midPoint = start + (end-1) // 2

        if(numberArray[midPoint] == number):
            return True

        if(numberArray[midPoint] < number):
            start = midPoint + 1
        else:
            end = midPoint - 1
    print(numberArray[midPoint])
    return numberArray[midPoint] == number

def isPrime(n):
    for i in range(2, int(n**(0.5)) + 1):
        if(n % i == 0):
            return False
    return True

def primesum(A):
    for i in range(2, A//2 + 1):
        if(isPrime(i)):
            b = A - i
            if(isPrime(b)):
                return [i, b]

print(primesum(1048574))
print(primesum(4))