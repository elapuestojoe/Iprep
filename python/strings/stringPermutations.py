'''
Generates all permutations of a string (assumes unique characters)
'''

def permute(a, l, r):
    if(l==r):
        print("".join(a))
    else:
        for i in range(l, r+1): 
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

string = "abcd"
l = list(string)
n = len(string)
permute(l, 0, n-1)

