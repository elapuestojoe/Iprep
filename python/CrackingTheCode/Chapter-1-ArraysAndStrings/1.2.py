'''
Write code to reverse a C-Style String 
(C-String means that “abcd” is represented as five characters, including the null character )
'''

def reverseCString(s):
    print("reverseCString {}".format(s))
    left = 0
    end = 0

    # Validation
    if(s[end] is None):
        return [None]

    while(s[end+1] is not None):
        end+=1
    
    while(left < end):
        s[left], s[end] = s[end], s[left]
        left+=1
        end-=1
    return s
    

a = list("C-Style-String")
a.append(None)
print(reverseCString(a))
print(reverseCString([None]))
print(reverseCString(["a", None]))
print(reverseCString(["a", "b", None]))