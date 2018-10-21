'''
Explain what the following code does: ((n & (n-1)) == 0)

n & (n-1) gets the leftmost bit in a bit sequence, if it is zero it means that n is a power of 2
'''

def isPowerOfTwo(n):
    return (n & (n-1)) == 0

for i in range(17):
    print(i, isPowerOfTwo(i))