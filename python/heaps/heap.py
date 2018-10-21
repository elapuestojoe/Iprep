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


myHeap = MinHeap()
myHeap.push(1)
myHeap.push(7)
myHeap.push(0)
myHeap.push(2)
myHeap.push(10)

sortedArr = []
while(not myHeap.isEmpty()):
    sortedArr.append(myHeap.pop())

print(sortedArr)