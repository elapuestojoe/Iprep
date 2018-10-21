def getVal(a, b):
    valA = 0
    valB = 0
    for i in range(len(a)):
        valA += (2**i) * a[i]
        valB += (2**i) * b[i]
    return valA - valB

def computePermutations(l1, l2):
    permutations = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            solution = []
            x = 0
            y = 0
            while(x < len(l1) and y < len(l2)):
                solution.append(l1[x])
                solution.append(l2[y])
                x += 1
                y += 1
            
            if(x < len(l1)):
                solution.append(l1[x])
            if(y < len(l2)):
                solution.append(l2[y])
            
            permutations.append(solution)
            l2 = l2[1:] + [l2[0]]
        l1 = l1[1:] + [l1[0]]
    return permutations

def alternatingParityPermutations(n):
    solutions = []
    even = []
    odd = []
    for i in range(1, n+1):
        if(i & 1):
            odd.append(i)
        else:
            even.append(i)

    solutions += computePermutations(odd, even)
    solutions += computePermutations(even, odd)
    
    solutions.sort()
    return solutions

# print(alternatingParityPermutations(3))

import itertools
print(list(itertools.permutations([1,2,3,4])))