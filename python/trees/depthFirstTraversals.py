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
    myBTree.root = Node(1)
    
    left = Node(2)
    left.left = Node(4)
    left.right = Node(5)
    myBTree.root.left = left

    myBTree.root.right = Node(3)

    return myBTree

def InOrderTraversal(node):
    if(node is not None):
        
        InOrderTraversal(node.left)
        print(node.value)
        InOrderTraversal(node.right)

def PreOrderTraversal(node):
    if(node is not None):
        print(node.value)
        PreOrderTraversal(node.left)
        PreOrderTraversal(node.right)

def PostOrderTraversal(node):
    if(node is not None):
        PostOrderTraversal(node.left)
        PostOrderTraversal(node.right)
        print(node.value)

myTree = TreeConstruction()
InOrderTraversal(myTree.root)
print("-")
PreOrderTraversal(myTree.root)
print("-")
PostOrderTraversal(myTree.root)