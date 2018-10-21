import math

import time
def efficientRoadNetworkFloyd(n, roads):
    # Apply Floyd Warshall algorithm (n^3)
    solution = []
    for i in range(n):
        solution.append([4 for i in range(n)])
    for i in range(n):
        solution[i][i] = 0
    
    for road in roads:
        solution[road[0]][road[1]] = 1
        solution[road[1]][road[0]] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                solution[i][j] = min(solution[i][j], solution[i][k] + solution[k][j])
    
    for i in range(n):
        for j in range(i, n):
            if(solution[i][j] > 2):
                return False
    return True

def expandVertex(i, visited, adjacencyList, level, maxLevel):
    if(level < maxLevel and (not visited[i])):
        visited[i] = True
        for edge in adjacencyList[i]:
            expandVertex(edge, visited, adjacencyList, level+1, maxLevel)

def efficientRoadNetwork(n, roads):
    # DO BFS on n levels O(V^2)
    
    #Build adjacency list
    adjacencyList = []
    for i in range(n):
        adjacencyList.append([])
    for road in roads:
        adjacencyList[road[0]].append(road[1])
        adjacencyList[road[1]].append(road[0])
    
    for i in range(n): #O(V)
        visited = [False]*n

        expandVertex(i, visited, adjacencyList, 0, 3) #O(V)
        for i in range(len(visited)):
            if(not visited[i]):
                return False
    return True


# roads = [[3, 0], [0, 4], [5, 0], [2, 1],
#           [1, 4], [2, 3], [5, 2]]
# print(efficientRoadNetwork(6, roads))

# roads = [[0, 4], [5, 0], [2, 1],
#           [1, 4], [2, 3], [5, 2]]
# print(efficientRoadNetwork(6, roads))

# roads = [[3,0], 
#  [0,4], 
#  [5,0], 
#  [2,1], 
#  [1,4], 
#  [2,3], 
#  [5,2]]

# print(efficientRoadNetwork(6, roads))

roads =  [[7,12], 
 [3,15], 
 [0,7], 
 [14,1], 
 [15,6], 
 [8,7], 
 [3,4], 
 [1,3], 
 [15,2], 
 [2,11], 
 [1,8], 
 [12,0], 
 [7,4], 
 [9,5], 
 [11,10], 
 [7,5], 
 [6,11], 
 [5,15], 
 [1,12], 
 [4,15], 
 [6,4], 
 [11,7], 
 [4,8], 
 [10,15], 
 [1,7], 
 [3,13], 
 [15,7], 
 [13,4], 
 [13,6], 
 [12,10], 
 [1,13], 
 [6,14], 
 [4,0], 
 [11,1], 
 [13,15], 
 [10,2], 
 [6,9], 
 [0,13], 
 [8,6], 
 [14,9], 
 [13,5], 
 [14,7], 
 [13,9], 
 [6,7], 
 [9,10], 
 [8,2], 
 [12,8], 
 [9,3], 
 [11,15], 
 [12,13], 
 [2,0], 
 [9,0], 
 [3,8], 
 [15,14], 
 [1,9], 
 [1,2], 
 [3,12]]
# print(efficientRoadNetwork(16, roads))

start = time.time()
a = efficientRoadNetwork(16, roads)
end = time.time()
print(end-start)

start = time.time()
b = efficientRoadNetworkFloyd(16, roads)
end = time.time()
print(end-start)

print(a)
print(b)