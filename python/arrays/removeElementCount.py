def removeElement(A, B):
    size = len(A)
    elements = 0
    for i in range(size):
        if(A[i] == B):
            elements += 1
        else:
            A[i], A[i-elements] = A[i-elements], A[i]
    return size-elements


a = [4,1,1,2,1,3]
print(removeElement(a, 1))
print(a)
b = [0,0,0,0,0]
print(removeElement(b, 1))
print(b)