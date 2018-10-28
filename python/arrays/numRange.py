# @param A : list of integers
# @param B : integer
# @param C : integer
# @return an integer

def numRangeA(A, B, C):
    i = 0
    j = 0
    accumulator = 0
    solutions = 0
    while(i < len(A)):
        accumulator += A[j]
        
        if((accumulator >= B and accumulator <= C)):
            solutions += 1
            j+=1
        elif(accumulator < B):
            j+=1
        elif(accumulator > C):
            i+=1
            j = i
            accumulator = 0
        if(j == len(A)):
            accumulator = 0
            i+=1
            j = i
    return solutions

def numRange(A, B, C):
    i = 0
    j = 0
    accumulator = 0
    solutions = 0
    while(i < len(A) and j < len(A)):

        if(i==j):
            accumulator = A[i]
        print(i,j, accumulator)
        if(accumulator >= B and accumulator <= C):

            solutions += 1

            if(j < len(A)-1):
                if(accumulator + A[j+1] <= C):
                    accumulator += A[j+1]
                    j+=1
                
                else:
                    if(i==j):
                        i+=1
                        j+=1
                    else:
                        i+=1
                        j = i
            else:
                i+=1
                j = i

        elif(accumulator > C):
            if(i==j):
                i+=1
                j+=1
            else:
                i+=1
                j = 1
        elif(accumulator < B):
            if(j < len(A) -1):
                accumulator += A[j+1]
                j+=1
            else:
                return solutions
    return solutions

print(numRange([10,2,4,1,0,0,7,9], 2, 9))
print(numRange([10,5,1,0,2], 6, 8))

print(numRangeA([10,2,4,1,0,0,7,9], 2, 9))
print(numRangeA([10,5,1,0,2], 6, 8))