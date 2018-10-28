def setColumnsRows(matrix, i, n):
    for x in range(i, len(matrix[0])-i):
        matrix[i][x] = n-i
        matrix[len(matrix)-i-1][x] = n-i
    for y in range(i, len(matrix)-i):
        matrix[y][i] = n-i
        matrix[y][len(matrix[0])-i-1] = n-i

def prettyPrint(A):

    width = (A * 2) - 1
    height = (A * 2) - 1

    matrix = []
    for i in range(height):
        matrix.append([0]*width)

    for i in range(A):
        setColumnsRows(matrix, i, A)
    return matrix

for i in range(0,6):
    result = prettyPrint(i)
    if len(result) == 0:
        print([])
    for column in result:
        print(column)