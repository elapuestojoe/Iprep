'''
Note: Try to solve this task in O(m + n) or O(n) time, where n is a number of vertices and m is a number of edges, since this is what you'll be asked to do during an interview.

In a multithreaded environment, it's possible that different processes will need to use the same resource. A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

Example

    For connections = [[1], [2], [3, 4], [4], [0]], the output should be
    hasDeadlock(connections) = true.
'''

def isCyclic(i, visited, stack, connections):
    visited[i] = True
    stack[i] = True
    
    for c in connections[i]:
        if(not visited[c]):
            if(isCyclic(c, visited, stack, connections)):
                return True
        elif stack[c]:
            return True
    stack[i] = False
    return False
    
def hasDeadlock(connections):
    visited = [False]*len(connections)
    stack = [False]*len(connections)
    
    for i in range(len(connections)):
        if(not visited[i]):
            if(isCyclic(i, visited, stack, connections)):
                return True
    return False