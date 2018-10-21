''' Write a program to swap odd and even bits in an integer with as few instructions as possible.
'''

def swapBits(A):
    i = 0
    n = 0
    while(A > 0):
        b = A & 1
        A = A >> 1
        b2 = A & 1
        A = A >> 1
        n += b2 << i
        n += b << i + 1
        i += 2
    return n

print(bin(10))
print(bin(swapBits(10)))

print(bin(15))
print(bin(swapBits(15)))

print(bin(31))
print(bin(swapBits(31)))