class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class List(object):
    def __init__(self):
        self.head = None

    def insert(self, node):
        it = self.head

        if(it is None):
            self.head = node
        else:
            while(it.next is not None):
                it = it.next
            it.next = node

    def display(self):
        it = self.head
        while(it is not None):
            print(it.value, end=",")
            it = it.next

        print(it)

def reverseList(myList):
    previous = None
    it = myList.head
    while(it is not None):
        temp = it.next
        it.next = previous
        previous = it
        it = temp

    myList.head = previous

if __name__ == "__main__":
    emptyList = List()

    oneElementList = List()
    oneElementList.insert(Node(5))

    emptyList.display()
    reverseList(emptyList)
    emptyList.display()

    oneElementList.display()
    reverseList(oneElementList)
    oneElementList.display()

    multipleElementList = List()
    for i in range(10):
        multipleElementList.insert(Node(i))
    multipleElementList.display()
    reverseList(multipleElementList)
    multipleElementList.display()
