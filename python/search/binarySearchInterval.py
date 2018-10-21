def binarySearchLeft(arr, value):
    left = 0
    right = len(arr) - 1
    while(left +1 < right):
        midPoint = (left+right)//2
        if(arr[midPoint]<value):
            left = midPoint+1
        else:
            right = midPoint
    
    if(arr[left]==value):
        return left
    elif(arr[right]==value):
        return right
    return -1
def binarySearchRight(arr, value):
    left = 0
    right = len(arr) - 1
    while(left + 1 < right):
        midPoint = (left+right)//2
        if(arr[midPoint]>value):
            right = midPoint-1
        else:
            left = midPoint
    if(arr[right]==value):
        return right
    elif(arr[left]==value):
        return left
    return -1
def countOccurences(arr, value):
    left = binarySearchLeft(arr, value)
    if(left != -1):
        return [left, binarySearchRight(arr, value)]
    else:
        return [-1, -1]
arr = [1,2,3,4,5,5,5,5,5,5,6,7,8,9,10,10]
arr2 = [1,1,1,1,1,10]
arr3 = [1,10,10,10,10,10]
arr4 = [1,2,3,5,5,5,5,5,5,6,7,8,9,10,10]
arr5 = [4,7,7,7,8,10,10]

print(countOccurences(arr, 5))
print(countOccurences(arr2,1))
print(countOccurences(arr2,10))
print(countOccurences(arr2, 11))
print(countOccurences(arr3, 1))
print(countOccurences(arr3, 10))
print(countOccurences(arr, 10))
print(countOccurences(arr4, 4))
print(countOccurences(arr5, 3))