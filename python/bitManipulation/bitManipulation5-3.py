'''Given an integer, print the next smallest and 
next largest number that have the same number of
1 bits in their binary rempresentation
'''

def nextSmallestAndLargest(value):
    i = 0
    j = 0
    while(not value & 1):
        value = value >> 1
        i += 1
    while(value & 1):
        

    value = value << i
    return value
print(bin(nextSmallestAndLargest(0b10100)))