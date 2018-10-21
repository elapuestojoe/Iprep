'''
Implement an algorithm to determine if a string has all unique characters What if you
can not use additional data structures?
'''

# Using additional data structures
# Space Complexity O(m), where M is the lenght of the character set
# Time Complexity O(n)
def hasUniqueCharactersAdditionalDataStructures(s):
    print("hasUniqueCharactersAdditionalDataStructures: {}".format(s))
    buckets = [0]*256
    for char in s:
        code = ord(char)
        buckets[code] += 1
        if (buckets[code] == 2):
            return False
    return True

print(hasUniqueCharactersAdditionalDataStructures("abcdefg"))
print(hasUniqueCharactersAdditionalDataStructures("abcdefgg"))

# If we assume that it only has lowercase characters we can replace buckets with a single int
def hasUnisqueCharactersUsingByte(s):
    print("hasUnisqueCharactersUsingByte: {}".format(s))
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if(checker & (1 << val)):
            return False 
        checker = checker | (1 << val)
    
    return True
print(hasUnisqueCharactersUsingByte("abcde"))
print(hasUnisqueCharactersUsingByte("abcdea"))

# Without using additional data structures
# Space Complexity O(1)
# Time Complecity O(n^2)
def hasUnisqueCharactersNoDataStructures(s):
    print("hasUnisqueCharactersNoDataStructures: {}".format(s))
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True
print(hasUnisqueCharactersNoDataStructures("djshreiwd"))
print(hasUnisqueCharactersNoDataStructures("djshreiw"))

# Sorting without using extra space would require that the string would be a list of chars