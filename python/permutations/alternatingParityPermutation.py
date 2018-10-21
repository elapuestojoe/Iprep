
class Node(object):
    def __init__(self, value, options, used):
        self.value = value
        self.options = options
        self.used = used
        self.children = []

def populateNode(node):
    for option in node.options:
        if(option & 1 != node.value & 1):
            otherOptions = []
            for op in node.options:
                if(op != option):
                    otherOptions.append(op)
            newNode = Node(option, otherOptions, node.used + [option])
            populateNode(newNode)
            node.children.append(newNode)

def iterateNode(node):
    if(len(node.children) == 0):
        print(node.used)
    else:
        for child in node.children:
            iterateNode(child)

def alternatingParityPermutation(n):
    initialOptions = [i for i in range(1, n+1)]

    nodes = []
    for option in initialOptions:
        otherOptions = []
        for i in range(len(initialOptions)):
            if(initialOptions[i] != option):
                otherOptions.append(initialOptions[i])
        nodes.append(Node(option, otherOptions, [option]))
    
    for node in nodes:
        populateNode(node)

    solution = []
    for node in nodes:
        iterateNode(node)
    return solution

print(alternatingParityPermutation(5))