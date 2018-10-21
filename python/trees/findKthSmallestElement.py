''' Gets kth smallest element using O(1) space in O(n) time using Morris Traversal'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if(self.root is None):
            self.root = Node(value)
        else:
            self.insertRecursively(self.root, value)

    def insertRecursively(self, node, value):
        if(value < node.value):
            if(node.left is None):
                node.left = Node(value)
            else:
                self.insertRecursively(node.left, value)
        elif(value > node.value):
            if(node.right is None):
                node.right = Node(value)
            else:
                self.insertRecursively(node.right, value)

    def DFSPrint(self):
        self.DFSPrintRecursive(self.root)

    def DFSPrintRecursive(self, node):
        if(node is not None):
            if(node.left is not None):
                self.DFSPrintRecursive(node.left)
            
            if(node.left is not None):
                self.DFSPrintRecursive(node.right)

            print(node.value)



def arrayToBST(array):
    bst = BST()
    for i in array:
        bst.insert(i)
    bst.DFSPrint()
    return bst

array = [5,4,3,7,9,2,-1]
bst = arrayToBST(array)

def kthSmallestInBST(t, k):
    current = t
    value = None
    while(current is not None):
        if(current.left is None):
            k -= 1
            if(k == 0):
                value = current.value
            current = current.right
        else:
            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right
            
            if(pre.right is None):
                pre.right = current
                current = current.left
            else:
                pre.right = None
                k -= 1
                if(k == 0):
                    value = current.value
                current = current.right
    return value

print("DRIVER")    
print(kthSmallestInBST(bst.root, 3))