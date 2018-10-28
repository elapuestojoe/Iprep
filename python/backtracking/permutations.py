'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
'''

def permute(arr, start, end):
    solutions = []
    if(start == end):
        return [arr.copy()]
    else:
        for j in range(start, end+1):
            arr[start], arr[j] = arr[j], arr[start]
            permutations = permute(arr, start+1, end)
            for permutation in permutations:
                solutions.append(permutation)
            arr[start], arr[j] = arr[j], arr[start]
    return solutions

def permutations(arr):
    return permute(arr, 0, len(arr)-1)

print(permutations([1,2,3]))
print(permutations([1]))
print(permutations([]))
print(permutations([1,2]))