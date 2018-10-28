'''
1- x & (x-1) will clear the lowest set bit of x
2- x & ~(x-1) extracts the lowest set bit of x (all others are clear). Pretty patterns when applied to a linear sequence.
3- x & (x + (1 << n)) = x, with the run of set bits (possibly length 0) starting at bit n cleared.
4- x & ~(x + (1 << n)) = the run of set bits (possibly length 0) in x, starting at bit n.
5- x | (x + 1) = x with the lowest cleared bit set.
6- x | ~(x + 1) = extracts the lowest cleared bit of x (all others are set).
7- x | (x - (1 << n)) = x, with the run of cleared bits (possibly length 0) starting at bit n set.
8- x | ~(x - (1 << n)) = the lowest run of cleared bits (possibly length 0) in x, starting at bit n are the only clear bits.
'''

def clearLowest(n):
    return n & (n-1)

print("1- Clear lowest: n & (n-1)")
print(bin(10), bin(clearLowest(10)))

def extractLowestSetBit(n):
    return n & ~(n-1)

print("2- Extract Lowest bit: n & ~(n-1)")
print(bin(22), bin(extractLowestSetBit(22)))
print(bin(31), bin(extractLowestSetBit(31)))
print(bin(32), bin(extractLowestSetBit(32)))

def clearBits(n, i):
    return n & (n + (1 << i))

print("3- Clear bit at position i")
print(bin(31),0, bin(clearBits(31, 0)))
print(bin(31),3, bin(clearBits(31, 3)))
print(bin(43),1, bin(clearBits(43, 1)))
print(bin(43),0, bin(clearBits(43, 0)))
print(bin(23),0, bin(clearBits(23, 0)))
print(bin(23),1, bin(clearBits(23, 1)))
print(bin(23),3, bin(clearBits(23, 3)))

def runOfBits(n, i):
    return n & ~(n + (1 << i))

print("4- Run of set bits")
print(bin(23), 0, bin(runOfBits(23, 0)))
print(bin(23), 1, bin(runOfBits(23, 1)))
print(bin(23), 2, bin(runOfBits(23, 2)))
print(bin(23), 3, bin(runOfBits(23, 3)))
print(bin(23), 4, bin(runOfBits(23, 4)))

def nLowestClearedBitSet(n):
    return n | (n+1)

print("5- x with lowest cleared bit set")
print(bin(23), bin(nLowestClearedBitSet(23)))
print(bin(89), bin(nLowestClearedBitSet(89)))
print(bin(31), bin(nLowestClearedBitSet(31)))

# TODO FIX
def extractLowestClearedBit(n):
    return n | ~(n+1)

print("6- Extract lowest cleared bit")
print(bin(9), bin(extractLowestClearedBit(9)))

def nWithRunOfClearedBitsSet(n, i):
    return n | (n - (1 << i))
print("7- X with the run of cleared bits starting at bit i set")
print(bin(44), bin(nWithRunOfClearedBitsSet(44, 0)))
print(bin(44), bin(nWithRunOfClearedBitsSet(44, 1)))
print(bin(44), bin(nWithRunOfClearedBitsSet(44, 2)))

def lowestRunOfClearedBitsInX(n, i):
    return n | ~(n - (1 << i))

print("8- The lowest run of cleared bits in x startign at i")
print(bin(44), bin(lowestRunOfClearedBitsInX(44, 0)))
print(bin(44), bin(lowestRunOfClearedBitsInX(44, 4)))