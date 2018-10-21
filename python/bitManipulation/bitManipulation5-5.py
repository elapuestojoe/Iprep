'''
Write a function to determine the number of bits required to convert integer A to
integer B
Input: 31, 14
Output: 2
'''

def numberOfBitsToConvert(A, B):
    # xor to get different bits
    c = A ^ B
    result = 0

    # Get rightmost bit and increase result
    while c > 0:
        c = c & (c-1)
        result += 1
    return result

print(numberOfBitsToConvert(31, 14))