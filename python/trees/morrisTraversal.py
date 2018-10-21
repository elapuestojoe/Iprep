'''
Used for inorder binary search tree traversal with O(1) extra space
'''
import random
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    
    def insertRecursive(self, value, node):
        if(value < node.value):
            if(node.left is None):
                node.left = Node(value)
            else:
                self.insertRecursive(value, node.left)
        elif(value > node.value):
            if(node.right is None):
                node.right = Node(value)
            else:
                self.insertRecursive(value, node.right)

    def insert(self, value):
        if(self.root is None):
            self.root = Node(value)
        else:
            self.insertRecursive(value, self.root)


def RecursiveBFS(node):
    if(node is not None):
        if(node.left is not None):
            RecursiveBFS(node.left)
        
        print(node.value)

        if(node.right is not None):
            RecursiveBFS(node.right)

def MorrisTraversal(root):

    current = root

    while(current is not None):
        if(current.left is None):
            print(current.value)
            current = current.right
        else:
            #Find inorder predecessor (top right most element from left subtree)
            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right
            
            #Set current as right child of its predecessor
            if(pre.right is None):
                pre.right = current
                current = current.left
            #revert the changes made in if part to restore
            #original tree
            else:
                pre.right = None
                print(current.value)
                current = current.right

myTree = BST()
for i in range(5):
    val = int(random.random()*100%100)
    myTree.insert(val)

RecursiveBFS(myTree.root)
print("-")
MorrisTraversal(myTree.root)



