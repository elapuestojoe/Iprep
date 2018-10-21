#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     

def checkSum(n, s, acc):
    
    if(n is not None):
        if(n.left is None and n.right is None):
            return n.value + acc == s
        else:
            a = False
            b = False
            if(n.left is not None):
                a = checkSum(n.left, s, acc + n.value)
            if(n.right is not None):
                b = checkSum(n.right, s, acc + n.value)
            return a or b
    else:
        return False
    
def hasPathWithGivenSum(t, s):
    return checkSum(t, s, 0)