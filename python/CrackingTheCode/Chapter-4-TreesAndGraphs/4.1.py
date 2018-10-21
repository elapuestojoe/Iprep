class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

'''
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.
'''

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


'''Subproblem:
Determine height of a node in a binary tree
'''

def getHeight(node):
    if(node is None):
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return 1 + max(getHeight(node.left), getHeight(node.right))

root = Node(1)
root.left=Node(3)
root.right=Node(2)

root.right.right=Node(4)

root.right.right.left = Node(5)
# print(getHeight(root))

root = Node(1)
root.left = Node(3)
root.right = Node(4)
print(isBalanced(root))