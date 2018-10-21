def binarySearch(arr, value):
    start = 0
    end = len(arr)-1
    while(start < end):
        midPoint = (start+end)//2
        if(arr[midPoint]==value):
            return midPoint
        elif(arr[midPoint] < value):
            start = midPoint+1
        else:
            end = midPoint-1
    if(len(arr) > 0 and arr[start]==value):
        return start
    else:
        return -1
arr = [1,2,3,4,5,5,5,5,5,5,6,7,8,9,10]
print(binarySearch(arr, 5))
print(binarySearch(arr,1))
print(binarySearch(arr,10))