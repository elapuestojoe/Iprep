'''
Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

def inOrder(tree):
    if(tree is not None):
        inOrder(tree.left)
        print(tree.value)
        inOrder(tree.right)
def preOrder(node):
    if(node is not None):
        print(node.value)
        preOrder(node.left)
        preOrder(node.right)

def isBalanced(node):
    if(node is None):
        return 0
    
    leftHeight = isBalanced(node.left)
    if(leftHeight == -1):
        return -1
    
    rightHeight = isBalanced(node.right)
    if(rightHeight == -1):
        return -1

    if(leftHeight > rightHeight + 1 or rightHeight > leftHeight + 1):
        return -1
    
    return (1 + max(leftHeight, rightHeight))


def arrayToBinaryTree(array, start, end):
    if(start <= end):
        midPoint = (start+end)//2
        root = Node(array[midPoint])
        root.left = arrayToBinaryTree(array, start, midPoint-1)
        root.right = arrayToBinaryTree(array, midPoint+1, end)

        return root
    else:
        return None

arr = [i for i in range(5)]
print(arr)

tree = arrayToBinaryTree(arr, 0, len(arr)-1)
# inOrder(tree)
# preOrder(tree)
print(isBalanced(tree))