def partition(arr, low, high):
    i = (low-1) #index of smaller element
    pivot = arr[high]

    for j in range(low, high):

        if(arr[j <= pivot]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if(low < high):

        partitioningIndex = partition(arr, low, high)
        quickSort(arr, low, partitioningIndex -1)
        quickSort(arr, partitioningIndex + 1, high)

    print(arr)
arr = [9, 7, 3, 21, -10, 0, 100]
n = len(arr)
quickSort(arr, 0, n-1)

for i in range(n):
    print(arr[i])