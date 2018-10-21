
def rotateMatrix(mat):
    N = len(mat)
    for x in range(N//2):
        for y in range(x, N-1-x):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]

            mat[N-1-y][x] = temp

def displayMat(mat):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            print(mat[x][y], end=" ")
        print("")
    print("-------")

matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [20,21,22,23,24]
]

displayMat(matrix)
rotateMatrix(matrix)
displayMat(matrix)