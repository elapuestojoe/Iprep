class DiGraph(object):
    def __init__(self):
        self.adjacencyList = {}

    def addEdge(self, a, b):
        if(a not in self.adjacencyList):
            self.adjacencyList[a] = [b]
        else:
            self.adjacencyList[a].append(b)
        
        if(b not in self.adjacencyList):
            self.adjacencyList[b] = []
    
    def display(self):
        print(self.adjacencyList)
        print(self.adjacencyList.keys())

    def BreathFirstTraversal(self):

        #VisitedArray
        visited = {}
        for node in self.adjacencyList.keys():
            visited[node] = False

        #Queue for BFS
        queue = []
        for node in self.adjacencyList.keys():
            queue.append(node)
            visited[node] = True

            while(len(queue)>0):

                current = queue.pop()
                print(current, end = "-")

                # Get adjacent values
                for neighbor in self.adjacencyList[current]:
                    if(not visited[neighbor]):
                        queue.append(neighbor)
                        visited[neighbor] = True

            print("")

    def BreathFirstTraversalFromNode(self, node):

        if(node not in self.adjacencyList):
            print("None")
            return

        visited = {}
        for n in self.adjacencyList:
            visited[n] = False
        
        visited[node] = True
        queue = []
        queue.append(node)
        while(len(queue)>0):
            current = queue.pop(0)
            print(current, end="-")
            for neighbor in self.adjacencyList[current]:
                if(not visited[neighbor]):
                    queue.append(neighbor)
                    visited[neighbor] = True
        print("")
    
    def DepthFirstTraversalUtil(self, node, visited):
        visited[node] = True
        print(node, end="-")

        #Recurr from all neighbors
        for neighbor in self.adjacencyList[node]:
            if(not visited[neighbor]):
                self.DepthFirstTraversalUtil(neighbor, visited)
    def DepthFirstTraversalFromNode(self, node):
        visited = {}
        for n in self.adjacencyList:
            visited[n] = False
        self.DepthFirstTraversalUtil(node, visited)
        print("")

diGraph = DiGraph()
diGraph.addEdge("a", "b")
diGraph.addEdge("a", "c")
diGraph.addEdge("c", "b")
diGraph.addEdge("a", "d")
diGraph.addEdge("d", "p")
diGraph.addEdge("b", "z")
diGraph.display()

diGraph.BreathFirstTraversalFromNode("a")
diGraph.DepthFirstTraversalFromNode("a")
# diGraph.BreathFirstTraversal()

# for node in diGraph.adjacencyList:
#     diGraph.BreathFirstTraversalFromNode(node)


