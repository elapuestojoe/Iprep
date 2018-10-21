#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def areNodesSymmetric(a, b):
    
    if(a is None and b is None):
        return True
    
    else:
        
        if(a is not None and b is not None):   
            return (a.value == b.value and areNodesSymmetric(a.left, b.right) and areNodesSymmetric(a.right, b.left))
        else:
            return a == b
    
def isTreeSymmetric(t):
    
    if(t is not None):
        return areNodesSymmetric(t.left, t.right)
    else:
        return True