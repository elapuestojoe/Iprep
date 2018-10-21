def selectionSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array
print(selectionSort([5,4,3,2,1]))