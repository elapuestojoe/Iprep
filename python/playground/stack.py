class Stack(object):
    def __init__(self):
        self.myList = list()
        self.valueCount = 0

    def push(self, value):
        self.myList.append(value)
        self.valueCount += 1

    def pop(self):
        if(self.valueCount > 0):
            self.valueCount -= 1
            return self.myList.pop()
        else:
            return None

if __name__ == "__main__":
    myStack = Stack()
    for i in range(10):
        myStack.push(i)

    val = myStack.pop()
    while(val is not None):
        print(val, end=",")
        val = myStack.pop()
    