'''
You are given two 32-bit numbers, N and M , and two bit positions, i and j.
Write a method to set all bits between i and j in N equal to M (e.g., M becomes a substring of N located at i and starting at j).
EXAMPLE:
Input: N = 10000000000, M= 10101, i=2, j=6
Output N = 10001010100
'''

def updateBits(N, M, i, j):
    maxN = (2**32)-1

    left = maxN - ((1 << j) - 1) # 1's from left to j, then 0
    right = ((1 << i) - 1) #1's from i to end
    mask = left | right

    #Apply mask to n and or with M shifted i times
    return bin((N & mask) | (M << i))

# print(updateBits(0b10000000000, 0b10101, 2, 6))
print(updateBits(0b11111111111, 0b10101, 2, 6))