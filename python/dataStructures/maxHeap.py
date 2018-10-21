class MaxHeap(object):
    def __init__(self, array):
        
        # Construct heap
        for i in range(1, len(array)):
            currentI = i
            parentI = int((currentI-1)/2)
            while(array[parentI] < array[currentI]):
                temp = array[parentI]
                array[parentI] = array[currentI]
                array[currentI] = temp
                currentI = parentI
                parentI = int((currentI-1)/2)

        self.heap = array
        self.size = len(array)
        
    def extractMax(self):
        max = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heap[self.size-1] = max
        self.size -= 1
        self.heapify(0)
        return max

    def heapify(self, i):
        largestIndex = i
        leftIndex = (i * 2) + 1
        rightIndex = (i * 2) + 2

        if(leftIndex < self.size and self.heap[leftIndex] > self.heap[largestIndex]):
            largestIndex = leftIndex

        if(rightIndex < self.size and self.heap[rightIndex] > self.heap[largestIndex]):
            largestIndex = rightIndex

        if(largestIndex != i):
            temp = self.heap[i]
            self.heap[i] = self.heap[largestIndex]
            self.heap[largestIndex] = temp
            self.heapify(largestIndex)


        
array = [35, 33, 42, 10, 14, 27, 44, 26, 31]

maxHeap = MaxHeap(array)
print(maxHeap.heap)
print(maxHeap.extractMax())
print(maxHeap.heap)
print(maxHeap.extractMax())
print(maxHeap.heap)