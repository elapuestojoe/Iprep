'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) 
participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers, 
each ranging from 0 to 255 inclusive, separated by dots, e.g., 172.16.254.1.

Given a string, find out if it satisfies the IPv4 address naming rules.
'''

def isIPv4Address(inputString):
    arr = inputString.split(".")
    
    if(len(arr) != 4):
        return False
    
    for i in range(len(arr)):
        if(arr[i] == ""):
            return False
        
        for c in arr[i]:
            if(ord(c) > 57):
                return False
        val = int(arr[i])
        if(val < 0 or val > 255 or str(val) != arr[i]):
            return False
    return True