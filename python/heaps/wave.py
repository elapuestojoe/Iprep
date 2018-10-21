class MinHeap(object):
    def __init__(self):
        self.heap = list()
    
    def push(self, value):
        self.heap.append(value)
        self.heapify(len(self.heap)-1)

    
    def heapify(self, i):
        continueFlag = True
        while (i > 0 and continueFlag):
            if(self.heap[i] < self.heap[(i-1)//2]):
                self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                i = (i-1)//2
            else:
                continueFlag = False

    def pop(self):
        if(not self.isEmpty()):
            minVal = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap.pop()
            
            self.rebalance(0)
            return minVal

        else:
            return None
    
    def rebalance(self, position):
        leftIndex = None
        rightIndex = None
        minIndex = None

        if((position*2)+1 < len(self.heap)):
            leftIndex = (position*2)+1
            minIndex = leftIndex
            if(leftIndex+1 < len(self.heap)):
                rightIndex = leftIndex + 1

                if(self.heap[rightIndex] < self.heap[leftIndex]):
                    minIndex = rightIndex
        
        if(minIndex):
            self.heap[position], self.heap[minIndex] = self.heap[minIndex], self.heap[position]
            self.rebalance(minIndex)
    
    def isEmpty(self):
        return len(self.heap) == 0
def wave(A):
    heap = MinHeap()
    for i in range(len(A)):
        heap.push(A[i])
        
    arr = []
    while(not heap.isEmpty()):
        arr.append(heap.pop())
    
    print(arr)
    stop = len(arr)
    if(stop & 1):
        stop -= 1
    for i in range(0, stop, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(wave([5,1,3,2,4]))