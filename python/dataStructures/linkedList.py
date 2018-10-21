class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List(object):
    def __init__(self, head: Node):
        self.head = head
    
    def insert(self, node: Node):
        iterator = self.head
        while(iterator is not None and iterator.next is not None):
            iterator = iterator.next
        
        iterator.next = node
    
    def display(self):
        iterator = self.head
        while(iterator is not None):
            print(iterator.data, end="")
            if(iterator.next is not None):
                print(", ", end = "")
            iterator = iterator.next
        print("")
# Initialize a list

myList = List(Node(10))
myList.insert(Node(6))
myList.insert(Node(2))
myList.display()