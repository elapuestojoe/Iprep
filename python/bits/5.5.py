''' Write a function to determine the number of bits required to convert integer A to integer B. 
Input: 31, 14
Output: 2
'''

def countBits(A, B):
    count = 0
    C = A ^ B
    while (C > 0):
        count += 1
        C = C & (C-1)
    return count

print(countBits(31,14))

# TODO: HANDLE negative numbers