'''
Write a method to replace all spaces in a string with ‘%20’
'''

def replaceSpaces(a):
    result = []
    for char in a:
        if(char == " "):
            result.append("%20")
        else:
            result.append(char)
    return "".join(result)

def replaceSpacesC(a):
    size = len(a)
    spaceCount = 0
    for i in range(size):
        if(a[i]== " "):
            spaceCount+=1
    
    if(spaceCount>0):
        newArr = [0]* (size + (spaceCount*2))
        i = 0
        j = 0
        while(i < size):
            if(a[i] == " "):
                newArr[j] = "%"
                newArr[j+1] = "2"
                newArr[j+2] = "0"
                j+= 3
            else:
                newArr[j] = a[i]
                j+=1
            i += 1
        return "".join(newArr)
    else:
        return a

print(replaceSpaces(" abc "))
print(replaceSpacesC(" abc "))
print(replaceSpacesC("abc"))
print(replaceSpacesC(" a b c "))