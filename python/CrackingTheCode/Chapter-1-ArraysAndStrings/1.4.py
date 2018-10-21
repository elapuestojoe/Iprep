'''
Write a method to decide if two strings are anagrams or not
'''

def areAnagrams(a, b):

    if(len(a) != len(b)):
        return False
    bucketA = [0]*128
    bucketB = [0]*128

    for i in range(len(a)):
        bucketA[ord(a[i])] += 1
        bucketB[ord(b[i])] += 1

    for i in range(128):
        if(bucketA[i] != bucketB[i]):
            return False
    return True

print(areAnagrams("abcdefgh", "abdcfehg"))
print(areAnagrams("abcdefgh", "abdcfehy"))