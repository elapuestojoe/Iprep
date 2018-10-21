def recursiveDFS(graph, startNode, visited=None):
    if(visited is None):
        visited = [False]*len(graph)
    visited[startNode] = True
    print(startNode)
    for node in graph[startNode]:
        if(not visited[node]):
            recursiveDFS(graph, node, visited)
    
def DFS(graph, startNode):
    visited = [False]*len(graph)
    stack = []
    stack.append(startNode)
    visited[startNode] = True

    while(len(stack)>0):
        vertex = stack.pop()
        # visited[startNode] = True
        print(vertex)
        for node in graph[vertex]:
            if(not visited[node]):
                stack.append(node)
                visited[node] = True
    

# Undirected graph (Skiena 162)
undirectedGraph = [
    [],
    [2,5,6],
    [1,3],
    [2,4],
    [3,5],
    [1,2],
    [1]
]

DFS(undirectedGraph, 1)
print("---")
recursiveDFS(undirectedGraph, 1)

