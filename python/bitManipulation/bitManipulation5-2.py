'''
Given a (decimal - e g 3 72) number that is passed in as a string, 
print the binary representation 
If the number can not be represented accurately in binary, print “ERROR”
'''

def printBinary(n):
    number = float(n)
    intPart = int(number)
    decimalPart = number-intPart

    int_string = ""
    while(intPart > 0):
        r = intPart & 1
        intPart = intPart >> 1
        int_string += str(r)
    
    decimal_buffer = []
    while(decimalPart > 0):
        if(len(decimal_buffer) > 32):
            return "ERROR"
        if(decimalPart == 1):
            decimal_buffer.append("1")
            decimalPart = 0
        else:
            r = decimalPart * 2
            if(r >= 1):
                decimal_buffer.append("1")
                decimalPart = r -1
            else:
                decimal_buffer.append("0")
                decimalPart = r
    decimal_string = "".join(decimal_buffer)
    return int_string+"."+decimal_string

print(printBinary("10.625"))
print(printBinary(3/5))