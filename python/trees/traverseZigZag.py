# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    
    def traverseZigZag(self, nodes, level):
        solutions = []
        
        levelArr = []
        nextLevel = []
        
        for i in range(len(nodes)):
            node = nodes[i]
            if(node.left is not None):
                nextLevel.append(node.left)
            if(node.right is not None):
                nextLevel.append(node.right)
        
        if(level%2!=0):
            nodes.reverse()
        
        for i in range(len(nodes)):
            levelArr.append(nodes[i].val)
        
        if(len(levelArr) > 0):
            solutions.append(levelArr)
        
        if(len(nextLevel) > 0):
            solutions+= (self.traverseZigZag(nextLevel, level+1))
        return solutions
        
    def zigzagLevelOrder(self, A):
        
        return self.traverseZigZag([A], 0)