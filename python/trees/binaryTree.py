class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self):
        self.root = None

def TreeConstruction():
    # Random tree used for testing
    myBTree = BinaryTree()
    
    aTemp = Node(-4)
    bTemp = Node(7)

    node = Node(-1)
    node.left = aTemp
    node.right = bTemp
    myBTree.root = Node(1)
    myBTree.root.right = node
    myBTree.root.left = Node(5)

    return myBTree

def BFS(node, value):
    if(node is not None):
        if(node.value == value):
            return True
        else:
            return BFS(node.left, value) or BFS(node.right, value)
    else:
        return False

def BFPrint(node):
    if(node is not None):
        print(node.value)
        BFPrint(node.left)
        BFPrint(node.right)

myTree = TreeConstruction()
BFPrint(myTree.root)
print(BFS(myTree.root, 7))