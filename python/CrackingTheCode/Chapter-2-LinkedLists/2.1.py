'''
Write code to remove duplicates from an unsorted linked list.
Follow up:
How would you solve this problem if a temporary buffer is not allowed?
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.root = None
    def insert(self, value):
        if(self.root is None):
            self.root = Node(value)
        else:
            i = self.root
            while(i.next is not None):
                i = i.next
            i.next = Node(value)
    def display(self):
        i = self.root
        while(i is not None):
            print(i.value, end=",")
            i = i.next
        print('')

def removeDuplicates(root):
    visited = {}
    if(root is None):
        return None
    
    visited[root.value] = True
    i = root
    while(i is not None and i.next is not None):
        if(i.next.value in visited):
            i.next = i.next.next
        else:
            visited[i.next.value] = True
            i = i.next

def improvedRemoveDuplicates(root):
    visited = {}
    previous = None
    i = root
    while(i):
        if(i.value in visited):
            previous.next = i.next
        else:
            visited[i.value] = True
            previous = i
        i = i.next

def removeDuplicatesNoBuffer(root):
    i = root
    while(i is not None):
        j = i
        while(i.next and i.next.value == i.value):
            i.next = i.next.next
        j = i.next
        while(j):
            if(j.next and j.next.value == i.value):
                j.next = j.next.next
            else:
                j = j.next
        i = i.next

myList = LinkedList()
myList.insert(1)
myList.insert(4)
myList.insert(4)
myList.insert(4)
myList.display()

# removeDuplicates(myList.root)
# removeDuplicatesNoBuffer(myList.root)
improvedRemoveDuplicates(myList.root)
myList.display()

# # 
# myList = LinkedList()
# myList.insert(1)
# myList.insert(1)
# myList.insert(1)
# myList.insert(1)
# myList.display()

# removeDuplicates(myList.root)
# myList.display()

# #
# myList = LinkedList()
# myList.display()

# removeDuplicates(myList.root)
# myList.display()

# #
# myList = LinkedList()
# myList.insert(1)
# myList.insert(2)
# myList.insert(1)
# myList.insert(1)
# myList.display()

# removeDuplicates(myList.root)
# myList.display()


