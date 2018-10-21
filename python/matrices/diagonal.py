def diagonal(matrix):
    solutions = []
    for x in range(0, len(matrix[0])):
        solution = []
        y = 0
        for tempX in range(x,-1,-1):
            solution.append(matrix[y][tempX])
            y += 1
        solutions.append(solution)
    
    for y in range(1, len(matrix)):
        solution = []
        x = len(matrix[0])-1
        for tempY in range(y, len(matrix)):
            solution.append(matrix[tempY][x])
            x -= 1
        solutions.append(solution)
    return solutions

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(diagonal(matrix))

matrix = [[1,2],[3,4]]
print(diagonal(matrix))