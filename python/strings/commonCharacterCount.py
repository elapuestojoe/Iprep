'''
Given two strings, find the number of common characters between them.
'''


def commonCharacterCount(s1, s2):
    bucketA = [0]*128
    bucketB = [0]*128

    commonCharacters = 0
    for char in s1:
        bucketA[ord(char)] += 1
    for char in s2:
        bucketB[ord(char)] += 1
    
    for i in range(len(bucketA)):
        commonCharacters += min(bucketA[i], bucketB[i])
    
    return commonCharacters

print(commonCharacterCount("aabcc", "adcaa"))
    