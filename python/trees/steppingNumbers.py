
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def populate(self, M):
        digit = self.value % 10
        nextVal = (self.value*10) + digit + 1
        prevVal = nextVal - 2
        
        if(nextVal <= M):
            if(digit < 9):
                self.right = Node(nextVal)
                self.right.populate(M)
        if(prevVal <= M):
            if(digit > 0):
                self.left = Node(prevVal)
                self.left.populate(M)
                
def DFS(node, N, M):
    solutions = []
    if(node is not None):

        leftSolutions = DFS(node.left, N, M)
        rightSolutions = DFS(node.right, N, M)

        if(node.value >= N and node.value <= M):
            solutions.append(node.value)

        for s in leftSolutions:
            solutions.append(s)
        for s in rightSolutions:
            solutions.append(s)


    
    return solutions
def steppingNumbers(N, M):

    if(N == 0):
        problemSolutions = [0]
    else:
        problemSolutions = []
    for i in range(1,10):
        node = Node(i)
        node.populate(M)
        solutions = DFS(node, N, M)
        for solution in solutions:
            problemSolutions.append(solution)
    return sorted(problemSolutions)

print(steppingNumbers(1, 101))

print(steppingNumbers(10, 20))