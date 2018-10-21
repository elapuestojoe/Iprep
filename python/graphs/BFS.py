def BFS(graph, startNode):
    visited = [False]*len(graph)
    parent = [None]*len(graph)

    visited[startNode] = True
    parent[startNode] = None #Not required but 

    queue = [startNode]
    while(len(queue)>0):
        current = queue.pop(0)
        print(current) # Process Vertex
        for edge in graph[current]:
            #Process edge
            if(not visited[edge]):
                visited[edge] = True
                parent[edge] = current
                queue.append(edge)
        
        # Set vertex as processed
    print(parent)

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

BFS(undirectedGraph, 1)
