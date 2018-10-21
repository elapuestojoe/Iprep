def getNthBit(value, i):
    return ((value & (1 << i)))

def setNthBit(value, i , b):
    if(b):
        return value | (1 << i)
    else:
        mask = ~(1 << index)
        return n & mask

# print(bin(getNthBit(0b10110, 3)))
# print(bin(setNthBit(0b0001, 3, 1)))
