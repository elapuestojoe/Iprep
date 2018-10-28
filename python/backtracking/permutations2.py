'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]
'''
def permute(arr, start, end):
    solutions = []
    if(start == end):
        return [arr.copy()]
    else:
        hashset = set()
        for j in range(start, end+1):
            if(arr[j] not in hashset):
                arr[start], arr[j] = arr[j], arr[start]
                permutations = permute(arr, start+1, end)
                for permutation in permutations:
                    solutions.append(permutation)
                arr[start], arr[j] = arr[j], arr[start]
                hashset.add(arr[j])
    return solutions

def permutations(arr):
    return permute(arr, 0, len(arr)-1)

print(permutations([1,2,3]))
print(permutations([1]))
print(permutations([]))
print(permutations([1,2]))
print(permutations([1,1,2]))
print(permutations([1,2,2]))