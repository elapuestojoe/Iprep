'''
Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer 
NOTE: One or two additional variables are fine  
An extra copy of the array is not FOLLOW UP Write the test cases for this method
'''

# Uses no space
# Time Complexity O(n^2)
# Space Complexity O(1)
def removeDuplicatesNoSpace(s):
    if(len(s) < 2):
        return s
    left = 0
    end = len(s)
    while(left < end):
        currentChar = s[left]
        i = left + 1
        skips = 0
        while(i < end):
            if(s[i]==currentChar):
                skips+=1
            else:
                s[i], s[i-skips] = s[i-skips], s[i]
            i+=1
        end-= skips
        left+=1
    return s[:end]

print(removeDuplicatesNoSpace(list("aabcccdefgaaa")))
print(removeDuplicatesNoSpace(list("abcdefg")))
print(removeDuplicatesNoSpace(list("aaaaa")))
print(removeDuplicatesNoSpace(list("abababab")))
print(removeDuplicatesNoSpace(list("")))
print(removeDuplicatesNoSpace(list("aa")))